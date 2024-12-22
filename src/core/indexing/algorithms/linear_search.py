from typing import List, Tuple
from src.core.indexing.base import BaseIndex
from scipy.spatial.distance import cosine


class LinearSearch(BaseIndex):
    def __init__(self):
        self.data = []

    def build_index(self, data: List[Tuple[str, list]]):
        """
        Build the index from a list of (id, embedding) tuples.
        """
        self.data = data

    def search(self, query_embedding: list, k: int) -> List[str]:
        """
        Search for the k-nearest neighbors of the query embedding.
        """

        # calculate cosine similarity for all embeddings
        similarities = [
            (id, 1 - cosine(query_embedding, embedding)) for id, embedding in self.data
        ]

        # sort by similarity and return the top k results
        similarities.sort(key=lambda x: x[1], reverse=True)
        return [id for id, _ in similarities[:k]]
