# Gensim 和 LDA
import gensim
from gensim.models import LdaModel
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
from gensim.models import CoherenceModel
from gensim.parsing.preprocessing import STOPWORDS
import pyLDAvis.gensim


def compute_coherence_values(dictionary, corpus, texts, limit, start=2, step=3):
    """
    计算c_v相干度为不同数量的主题
    Parameters:
    ----------
    dictionary : Gensim字典
    corpus : Gensim语料库
    texts : 输入文本的列表
    limit : 主题的最大数目
    Returns:
    -------
    model_list : LDA主题模型列表
    coherence_values : LDA模型相对应的相关值，对应于相应的主题数量
    """
    coherence_values = []
    model_list = []
    for num_topics in range(start, limit, step):
        model = gensim.models.wrappers.LdaMallet(mallet_path, corpus=corpus, num_topics=num_topics, id2word=dictionary)
        model_list.append(model)
        coherencemodel = CoherenceModel(model=model, texts=texts, dictionary=dictionary, coherence='c_v')
        coherence_values.append(coherencemodel.get_coherence())

    return model_list, coherence_values
    
if __name__ == '__main__':
    fp = open('data_without_POS.txt','r',encoding='utf8')
    data_2D_list = eval(fp.read())

    # -------------------------将待训练数据表示为词袋向量----------------------------
    # train = data_2D_list
    train = []
    train.extend(data_2D_list[0:101])
    dictionary = corpora.Dictionary(train)
    dictionary.filter_extremes(no_below=15, no_above=0.4, keep_n=80000)
    corpus = [dictionary.doc2bow(text) for text in train]

    # -------------------------训练LDA模型，并将训练出的n个类别存储在文件theme_class.txt中----------------------------
    # lda = LdaModel(corpus=corpus,
    #             id2word=dictionary,
    #             num_topics=10, 
    #             random_state=100,
    #             update_every=1,
    #             chunksize=100,
    #             passes=10,
    #             alpha='auto',
    #             per_word_topics=True)
    
    # with open('theme_class.txt', 'wt') as f:
    #     for topic in lda.print_topics(num_words = 20):
    #         termNumber = topic[0]
    #         print(topic[0], ':', file=f)
    #         listOfTerms = topic[1].split('+')
    #         for term in listOfTerms:
    #             listItems = term.split('*')
    #             print('  ', listItems[1], '(', listItems[0], ')', file=f)

    # # -------------------------用训练好的LDA模型对文本进行分类----------------------------
    # f2 = open('classify_result.txt', 'wt')
    # n = 0
    # for i in train:
    #     doc_bow = dictionary.doc2bow(i)
    #     doc_lda = lda[doc_bow]
    #     print(n, ': ', doc_lda, file=f2)
    #     n += 1
    # f2.close()

    # -------------------------输出评价指数----------------------------
    # f3 = open('judge.txt', 'wt')
    # # 计算困惑度 (分数越低越好)
    # print('困惑度（分数越低越好）: ', round(lda.log_perplexity(corpus), 2), file=f3)

    # # 计算连贯性 (分数越高越好)
    # coherence_model_lda = CoherenceModel(model=lda, texts=train, dictionary=dictionary, coherence='c_v')
    # coherence_lda = coherence_model_lda.get_coherence()
    # print('连贯性（分数越高越好）: ', round(coherence_lda, 2), file=f3)

    # f3.close()

    # # -------------------------图形可视化----------------------------
    # d = pyLDAvis.gensim.prepare(lda, corpus, dictionary)
    # pyLDAvis.save_html(d, 'lda_pass10.html')	# 将结果保存为该html文件
    # pyLDAvis.show(d, local=False, open_browser=True)
    
    # -------------------------优化----------------------------
    mallet_path = 'mallet-2.0.8/bin/mallet'
    # 注意:可能需要很长时间运行…
    model_list, coherence_values = compute_coherence_values(dictionary=dictionary, 
                                                        corpus=corpus, 
                                                        texts=train, 
                                                        start=8, 
                                                        limit=40, 
                                                        step=4)
    f4 = open('optimize.txt', 'wt')
    print(model_list, file=f4)
    print(coherence_values, file=f4)
    f4.close()
