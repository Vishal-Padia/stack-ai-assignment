from typing import List, Tuple
from src.core.indexing.base import BaseIndex
from sklearn.neighbors import KDTree


class KDTreeIndex(BaseIndex):
    def __init__(self):
        self.data = []
        self.tree = None
        self.ids = []

    def build_index(self, data: List[Tuple[str, list]]):
        """
        Build the index from a list of (id, embedding) tuples.
        """
        self.data = data
        self.ids, embeddings = zip(*data)
        self.tree = KDTree(embeddings)

    def search(self, query_embedding: list, k: int) -> List[str]:
        """
        Search for the k-nearest neighbors of the query embedding.
        """
        distances, indices = self.tree.query([query_embedding], k=k)
        return [self.ids[i] for i in indices[0]]
