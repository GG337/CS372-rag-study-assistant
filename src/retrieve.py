import faiss
import numpy as np

class Retriever:
    def __init__(self, embeddings, chunks):
        self.index = faiss.IndexFlatL2(len(embeddings[0]))
        self.index.add(np.array(embeddings))
        self.chunks = chunks

    def query(self, question_embedding, k=3):
        distances, indices = self.index.search(np.array([question_embedding]), k)
        return [self.chunks[i] for i in indices[0]]