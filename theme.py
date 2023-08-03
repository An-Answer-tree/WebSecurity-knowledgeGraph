from gensim import corpora
from gensim.models import LdaModel
from gensim.corpora import Dictionary
import pyLDAvis.gensim
from gensim.models import CoherenceModel

fp = open('data_without_POS.txt','r',encoding='utf8')
data_2D_list = eval(fp.read())

# -------------------------将待训练数据表示为词袋向量----------------------------
train = data_2D_list
dictionary = corpora.Dictionary(train)
corpus = [dictionary.doc2bow(text) for text in train]

# -------------------------训练LDA模型，并将训练出的n个类别存储在文件theme_class.txt中----------------------------
lda = LdaModel(corpus=corpus, id2word=dictionary, num_topics=10, passes=60)

with open('theme_class.txt', 'wt') as f:
    for topic in lda.print_topics(num_words = 20):
        termNumber = topic[0]
        print(topic[0], ':', file=f)
        listOfTerms = topic[1].split('+')
        for term in listOfTerms:
            listItems = term.split('*')
            print('  ', listItems[1], '(', listItems[0], ')', file=f)

# -------------------------用训练好的LDA模型对文本进行分类----------------------------
f2 = open('classify_result.txt', 'wt')
n = 0
for i in train:
    doc_bow = dictionary.doc2bow(i)      #文档转换成bow
    doc_lda = lda[doc_bow]
    print(n, ': ', doc_lda, file=f2)
    n += 1
f2.close()

# -------------------------图形可视化----------------------------
d=pyLDAvis.gensim.prepare(lda, corpus, dictionary)
pyLDAvis.save_html(d, 'lda_pass10.html')	# 将结果保存为该html文件
pyLDAvis.show(d)


# -------------------------输出评价指数----------------------------
f3 = open('judge.txt', 'wt')
# 计算困惑度 (分数越低越好)
print('困惑度（分数越低越好）: ', round(lda.log_perplexity(corpus), 2), file=f3)

# 计算连贯性 (分数越高越好)
coherence_model_lda = CoherenceModel(model=lda, texts=train, dictionary=dictionary, coherence='c_v')
coherence_lda = coherence_model_lda.get_coherence()
print('连贯性（分数越高越好）: ', round(coherence_lda, 2), file=f3)

f3.close()