# -------------------------------------------------导入库-----------------------------------------------------
import pandas as pd
from pprint import pprint

# Gensim
import gensim
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
from gensim.models import CoherenceModel

# Plotting tools
import matplotlib.pyplot as plt

# Enable logging for gensim - optional
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.ERROR)

import warnings
warnings.filterwarnings("ignore",category=DeprecationWarning)
mallet_path = 'mallet-2.0.8/bin/mallet'




# -------------------------------------------计算一致度函数定义--------------------------------------------------
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
        model = gensim.models.wrappers.LdaMallet(mallet_path, corpus=corpus, num_topics=num_topics, id2word=id2word)
        model_list.append(model)
        coherencemodel = CoherenceModel(model=model, texts=texts, dictionary=dictionary, coherence='c_v')
        coherence_values.append(coherencemodel.get_coherence())

    return model_list, coherence_values






# ----------------------------------------------------函数导入--------------------------------------------------
fp = open('./data_without_POS.txt','r',encoding='utf8')
data_2D_list = eval(fp.read())
train = data_2D_list
# train = []
# train.extend(data_2D_list[0:101])





# ----------------------------------------------将待训练数据表示为词袋向量-----------------------------------------
id2word = corpora.Dictionary(train)
id2word.filter_extremes(no_below=15, no_above=0.4, keep_n=80000)
corpus = [id2word.doc2bow(text) for text in train]





# # -----------------------------获取最优主题数（先注释掉此部分之后的所有内容，运行后获取最优主题）--------------------------
# # Can take a long time to run.
# model_list, coherence_values = compute_coherence_values(dictionary=id2word, corpus=corpus, texts=train, start=2, limit=40, step=6)
# # Show graph
# limit=40; start=2; step=6;
# x = range(start, limit, step)
# plt.plot(x, coherence_values)
# plt.xlabel("Num Topics")
# plt.ylabel("Coherence score")
# plt.legend(("coherence_values"), loc='best')
# plt.show()

# # Print the coherence scores
# for m, cv in zip(x, coherence_values):
#     print("Num Topics =", m, " has Coherence Value of", round(cv, 4))





# ---------------------------------------输出训练的n个主题（根据最优主题数更改num_topics）------------------------------
optimal_model = gensim.models.wrappers.LdaMallet(mallet_path, corpus=corpus, num_topics=36, id2word=id2word)
model_topics = optimal_model.show_topics(formatted=False)

# 打开文件以供写入
with open('output.txt', 'w') as file:
    # 将输出重定向到文件
    pprint(optimal_model.print_topics(num_topics=36, num_words=10), stream=file)





# -------------------------------------------------对目标语句进行主题分类-------------------------------------------------
def format_topics_sentences(ldamodel=optimal_model, corpus=corpus, texts=train):
    # Init output
    sent_topics_df = pd.DataFrame()

    # Get main topic in each document
    for i, row in enumerate(ldamodel[corpus]):
        row = sorted(row, key=lambda x: (x[1]), reverse=True)
        # Get the Dominant topic, Perc Contribution and Keywords for each document
        for j, (topic_num, prop_topic) in enumerate(row):
            if j == 0:  # => dominant topic
                wp = ldamodel.show_topic(topic_num)
                topic_keywords = ", ".join([word for word, prop in wp])
                sent_topics_df = sent_topics_df.append(pd.Series([int(topic_num), round(prop_topic,4), topic_keywords]), ignore_index=True)
            else:
                break
    sent_topics_df.columns = ['Dominant_Topic', 'Perc_Contribution', 'Topic_Keywords']

    # Add original text to the end of the output
    contents = pd.Series(texts)
    sent_topics_df = pd.concat([sent_topics_df, contents], axis=1)
    return(sent_topics_df)

df_topic_sents_keywords = format_topics_sentences(ldamodel=optimal_model, corpus=corpus, texts=train)

# Format
df_dominant_topic = df_topic_sents_keywords.reset_index()
df_dominant_topic.columns = ['Document_No', 'Dominant_Topic', 'Topic_Perc_Contrib', 'Keywords', 'Text']

# Show
df_dominant_topic.head(10)
df_dominant_topic.to_csv('filename.csv', index=False)