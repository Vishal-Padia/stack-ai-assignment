from abc import ABC, abstractmethod
from typing import List, Tuple


class BaseIndex(ABC):
    @abstractmethod
    def build_index(self, data: List[Tuple[str, list]]):
        """
        Build the index form a list of (id, embedding) tuples
        """
        pass

    @abstractmethod
    def search(self, query_embedding: list, k: int) -> List[str]:
        """
        Search for the k-nearest neighbors of the query embedding.
        """
        pass
