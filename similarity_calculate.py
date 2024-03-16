from sentence_transformers import SentenceTransformer
from scipy.spatial.distance import cosine
import numpy as np
import json
import time

# load model
model = SentenceTransformer('sbert-base-chinese-nli')
# use cuda
device = 'cuda'
model.to(device)

# load data
data = []
with open('data_after_ner_ssid.json', mode='rt', encoding='utf-8') as file:
    data = json.load(file)

contents = []
for i in range(0, 2818):
    contents.append(data[i]['content'])

start = time.time()
with open('similarity_scores.txt', 'a') as file:
    for i in range(1589, 2818):
        print("running i = ", i)
        reference_sentence = contents[i]
        sentences = contents[i:2818]

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
        file.flush()
end = time.time()
print('total time = ', end-start)
