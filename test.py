from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import paired_cosine_distances
import json
model = SentenceTransformer('sbert-base-chinese-nli')


sentences = ['', '']
sentence_embeddings = model.encode(sentences)

cosine_score = 1 - paired_cosine_distances([sentence_embeddings[0]],[sentence_embeddings[1]])
print(cosine_score)