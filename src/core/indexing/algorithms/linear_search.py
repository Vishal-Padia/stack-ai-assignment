import math
from typing import List, Tuple
from src.core.indexing.base import BaseIndex


class LinearSearch(BaseIndex):
    def __init__(self):
        self.data = []  # List of (id, embedding) tuples

    def build_index(self, data: List[Tuple[str, list]]):
        """
        Build the index from a list of (id, embedding) tuples.
        """
        self.data = data

    def search(self, query_embedding: list, k: int) -> List[str]:
        """
        Search for the k-nearest neighbors of the query embedding.
        """
        # Calculate the Euclidean distance for all embeddings
        distances = []
        for id, embedding in self.data:
            distance = self._euclidean_distance(query_embedding, embedding)
            distances.append((id, distance))

        # Sort by distance and return the top-k results
        distances.sort(key=lambda x: x[1])
        return [id for id, _ in distances[:k]]

    def _euclidean_distance(self, a: list, b: list) -> float:
        """
        Calculate the Euclidean distance between two vectors.
        """
        return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))
