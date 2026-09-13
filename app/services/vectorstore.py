import numpy as np


class VectorStore:
    def __init__(self):
        self.chunks = []
        self.embeddings = []

    def add(self, chunks, embeddings):
        self.chunks = chunks
        self.embeddings = np.array(embeddings)

    def search(self, query_embedding, top_k=3):
        query_embedding = np.array(query_embedding)

        similarities = np.dot(
            self.embeddings,
            query_embedding
        )

        top_indices = similarities.argsort()[-top_k:][::-1]

        return [self.chunks[i] for i in top_indices]


vector_store = VectorStore()