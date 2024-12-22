from typing import List, Tuple
from src.core.indexing.base import BaseIndex
from scipy.spatial.distance import euclidean


class BallTreeNode:
    def __init__(
        self,
        data: List[Tuple[str, list]],
        centroid: list,
        radius: float,
        left=None,
        right=None,
    ):
        self.data = data
        self.centroid = centroid  # Center of the ball
        self.radius = radius  # Radius of the ball
        self.left = left  # Left child
        self.right = right  # Right child


class BallTreeIndex(BaseIndex):
    def __init__(self):
        self.root = None

    def build_index(self, data: List[Tuple[str, list]]):
        """
        Build the Ball Tree index from a list of (id, embedding) tuples.
        """
        self.root = self._build_tree(list(data))

    def _build_tree(self, data: List[list]) -> BallTreeNode:
        """
        Recursively build the Ball Tree.
        """
        if not data:
            return None

        # Extract embeddings from the data
        embeddings = [embedding for _, embedding in data]

        # Find the centroid (mean of all points)
        centroid = [sum(dim) / len(dim) for dim in zip(*embeddings)]

        # Calculate the radius (max distance from centroid to any point)
        radius = max(euclidean(centroid, point) for point in embeddings)

        # Split the data into two halves based on distance from the centroid
        data.sort(key=lambda x: euclidean(x[1], centroid))
        mid = len(data) // 2

        # Recursively build left and right subtrees
        left = self._build_tree(data[:mid])
        right = self._build_tree(data[mid + 1 :])

        return BallTreeNode(data, centroid, radius, left, right)

    def search(self, query_embedding: list, k: int) -> List[str]:
        """
        Search for the k-nearest neighbors of the query embedding.
        """
        results = []
        self._search_tree(self.root, query_embedding, k, results)
        return [id for id, _ in sorted(results, key=lambda x: x[1])[:k]]

    def _search_tree(
        self, node: BallTreeNode, query: list, k: int, results: List[Tuple[int, float]]
    ):
        """
        Recursively search the Ball Tree for the nearest neighbors.
        """
        if node is None:
            return

        # Calculate the distance from the query to the centroid
        distance = euclidean(query, node.centroid)

        # If the query is inside the ball, explore both children
        if distance <= node.radius:
            self._search_tree(node.left, query, k, results)
            self._search_tree(node.right, query, k, results)

        # If the query is outside the ball, explore the closest child
        else:
            if node.left and euclidean(query, node.left.centroid) < euclidean(
                query, node.right.centroid
            ):
                self._search_tree(node.left, query, k, results)
            else:
                self._search_tree(node.right, query, k, results)

        # Add the current node's data to the results if it's one of the k-nearest neighbors
        for id, embedding in node.data:
            dist = euclidean(query, embedding)
            if len(results) < k:
                results.append((id, dist))
            else:
                max_distance = max(results, key=lambda x: x[1])[1]
                if dist < max_distance:
                    results.remove(max(results, key=lambda x: x[1]))
                    results.append((id, dist))
