from sentence_transformers import SentenceTransformer
from scipy.spatial.distance import cosine
import numpy as np
import json
import time
# load model
model = SentenceTransformer('sbert-base-chinese-nli')

# load data
data = []
with open('data_after_ner_ssid.json', mode='rt') as file:
    data = json.load(file)

contents = []
for i in range(0, 11):
    contents.append(data[i]['content'])

start = time.time()
with open('similarity_scores.txt', 'w') as file:
    for i in range(0, 11):
        reference_sentence = contents[i]
        sentences = contents[i:11]

        # 将参考文本和待比较文本列表转换为嵌入向量
        reference_embedding = model.encode(reference_sentence)
        sentence_embeddings = model.encode(sentences)

        # 计算每个待比较文本与参考文本的余弦相似度
        cosine_scores = []
        for embedding in sentence_embeddings:
            score = 1 - cosine(reference_embedding, embedding)
            print(score, ',', end='')
            cosine_scores.append(score)
        print()
        file.write(repr(cosine_scores) + ',\n')
        file.write(',')
        file.write('\n')
end = time.time()
print('total time = ', end-start)
    

# 打印相似度得分
# for i, score in enumerate(cosine_scores):
#     print(f"Similarity score between reference sentence and sentence {i + 1}: {score}")