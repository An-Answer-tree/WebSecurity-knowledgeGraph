from gensim import corpora
from gensim.models import LdaModel
from gensim.corpora import Dictionary

fp = open('data_without_POS.txt','r',encoding='utf8')
data_2D_list = eval(fp.read())

train = []
train.append(data_2D_list[0])
train.append(data_2D_list[1])

dictionary = corpora.Dictionary(train)

corpus = [dictionary.doc2bow(text) for text in train]

lda = LdaModel(corpus=corpus, id2word=dictionary, num_topics=20, passes=60)
# num_topics：主题数目
# passes：训练伦次
# num_words：每个主题下输出的term的数目

for topic in lda.print_topics(num_words = 20):
    termNumber = topic[0]
    print(topic[0], ':', sep='')
    listOfTerms = topic[1].split('+')
    for term in listOfTerms:
        listItems = term.split('*')
        print('  ', listItems[1], '(', listItems[0], ')', sep='')
