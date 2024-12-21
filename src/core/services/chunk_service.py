from typing import List, Optional
from src.core.models.chunk import Chunk


class ChunkService:
    def __init__(self):
        self.chunks: List[Chunk] = []

    def create_chunk(self, chunk: Chunk) -> Chunk:
        """
        Create a new Chunk
        """
        self.chunks.append(chunk)
        return chunk

    def get_chunk(self, chunk_id: str) -> Optional[Chunk]:
        """
        Get a Chunk by ID
        """
        return next((chk for chk in self.chunks if chk.id == chunk_id), None)

    def update_chunk(self, chunk_id: str, updated_chunk: Chunk) -> Optional[Chunk]:
        """
        Update a chunk by it's ID
        """
        for i, chk in enumerate(self.chunks):
            if chk.id == chunk_id:
                self.chunks[i] = updated_chunk
                return updated_chunk
        return None

    def delete_chunk(self, chunk_id: str) -> bool:
        """
        Delete a chunk by it's ID
        """
        for i, chk in enumerate(self.chunks):
            if chk.id == chunk_id:
                del self.chunks[i]
                return True
        return False
