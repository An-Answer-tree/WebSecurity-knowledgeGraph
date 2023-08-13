import gensim
from gensim.models import LdaModel
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
from gensim.models import CoherenceModel
from gensim.parsing.preprocessing import STOPWORDS
import pyLDAvis.gensim
from matplotlib.pylab import plt
def compute_coherence_values(dictionary, corpus, texts, limit, start=2, step=3):
    """
    Compute c_v coherence for various number of topics

    Parameters:
    ----------
    dictionary : Gensim dictionary
    corpus : Gensim corpus
    texts : List of input texts
    limit : Max num of topics

    Returns:
    -------
    model_list : List of LDA topic models
    coherence_values : Coherence values corresponding to the LDA model with respective number of topics
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
    mallet_path = 'mallet-2.0.8/bin/mallet'


    # Can take a long time to run.
    model_list, coherence_values = compute_coherence_values(dictionary=dictionary, corpus=corpus, texts=train, start=2, limit=40, step=4)
    # Show graph
    limit=40; start=2; step=4
    x = range(start, limit, step)
    plt.plot(x, coherence_values)
    plt.xlabel("Num Topics")
    plt.ylabel("Coherence score")
    plt.legend(("coherence_values"), loc='best')
    plt.show()

