from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import paired_cosine_distances
import json
# load model
model = SentenceTransformer('sbert-base-chinese-nli')

# load data
data = []
with open('data_after_ner_ssid.json', mode='rt') as file:
    data = json.load(file)

# print(data[0]['content'])

sentences = [data[0]['content'], data[1]['content']]
sentence_embeddings = model.encode(sentences)

cosine_score = 1 - paired_cosine_distances([sentence_embeddings[0]],[sentence_embeddings[1]])
print(cosine_score)