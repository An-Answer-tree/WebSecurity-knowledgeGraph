# LDA主题模型，用于对分词后的文档进行主题划分
1. 运行环境  
                gensim==3.8.3
                pandas==1.3.5
                pprint
                matplotlib
   
2. 代码说明
 2.1 数据要求
   原始数据要求为二维列表，外层列表的每个元素是一条语句，内层列表的每个元素为语句分词后的单词
 2.2 代码说明
   导入原始数据二维列表至data_2D_list，设置的训练用列表为train = data_2D_list。
  2.2.1 获取最优主题数
    应先运行“获取最优主题数”部分（lda_run.py中已用注释表示），运行这部分时，需要将“输出训练的n个主题”“对目标语句进行主题分类”注释掉。
  2.2.2 输出训练的n个主题，并对目标语句进行主题分类
    运行时，根据获取的最优主题数更改
            gensim.models.wrappers.LdaMallet(mallet_path, corpus=corpus, num_topics=36, id2word=id2word)
    中的num_topics。运行前需要注释掉“获取最优主题数”部分。
