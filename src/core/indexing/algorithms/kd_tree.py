import math
from typing import List, Tuple, Optional
from src.core.indexing.base import BaseIndex


class KDTreeNode:
    def __init__(self, point: Tuple[str, list], axis: int, left=None, right=None):
        self.point = point  # (id, embedding) tuple
        self.axis = axis  # The dimension to split on
        self.left = left  # Left child
        self.right = right  # Right child


class KDTreeIndex(BaseIndex):
    def __init__(self):
        self.root = None

    def build_index(self, data: List[Tuple[str, list]]):
        """
        Build the KD-Tree from a list of (id, embedding) tuples.
        """
        if not data:
            return
        self.root = self._build_tree(data, 0)

    def _build_tree(
        self, data: List[Tuple[str, list]], depth: int
    ) -> Optional[KDTreeNode]:
        """
        Recursively build the KD-Tree.
        """
        if not data:
            return None

        # Select axis based on depth so that axis cycles through all valid values
        axis = depth % len(data[0][1])

        # Sort points by the current axis and choose the median as the pivot
        data.sort(key=lambda x: x[1][axis])
        median = len(data) // 2

        # Create the node and recursively build subtrees
        return KDTreeNode(
            point=data[median],
            axis=axis,
            left=self._build_tree(data[:median], depth + 1),
            right=self._build_tree(data[median + 1 :], depth + 1),
        )

    def search(self, query_embedding: list, k: int) -> List[str]:
        """
        Search for the k-nearest neighbors of the query embedding.
        """
        if not self.root:
            return []

        # Track the k-nearest neighbors
        results = []
        self._search_tree(self.root, query_embedding, k, results)
        return [id for id, _ in sorted(results, key=lambda x: x[1])[:k]]

    def _search_tree(
        self, node: KDTreeNode, query: list, k: int, results: List[Tuple[str, float]]
    ):
        """
        Recursively search the KD-Tree for the nearest neighbors.
        """
        if not node:
            return

        # Calculate the Euclidean distance to the current node's point
        distance = self._euclidean_distance(query, node.point[1])

        # Add the current node's point to the results if it's one of the k-nearest neighbors
        if len(results) < k:
            results.append((node.point[0], distance))
        else:
            max_distance = max(results, key=lambda x: x[1])[1]
            if distance < max_distance:
                results.remove(max(results, key=lambda x: x[1]))
                results.append((node.point[0], distance))

        # Determine which subtree to explore first
        axis = node.axis
        if query[axis] < node.point[1][axis]:
            self._search_tree(node.left, query, k, results)
            # Check if there could be any points in the right subtree
            if (
                abs(query[axis] - node.point[1][axis])
                < max(results, key=lambda x: x[1])[1]
            ):
                self._search_tree(node.right, query, k, results)
        else:
            self._search_tree(node.right, query, k, results)
            # Check if there could be any points in the left subtree
            if (
                abs(query[axis] - node.point[1][axis])
                < max(results, key=lambda x: x[1])[1]
            ):
                self._search_tree(node.left, query, k, results)

    def _euclidean_distance(self, a: list, b: list) -> float:
        """
        Calculate the Euclidean distance between two vectors.
        """
        return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))
