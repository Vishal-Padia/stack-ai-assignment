from fastapi import APIRouter, HTTPException
from src.core.models.chunk import Chunk
from src.core.services.chunk_service import ChunkService

router = APIRouter()
chunk_service = ChunkService()


@router.post("/", response_model=Chunk)
def create_chunk(chunk: Chunk):
    """
    Create a new chunk
    """
    return chunk_service.create_chunk(chunk)


@router.get("/{chunk_id}", response_model=Chunk)
def get_chunk(chunk_id: str):
    """
    Get a chunk by id
    """
    chunk = chunk_service.get_chunk(chunk_id)
    if not chunk:
        raise HTTPException(status_code=404, detail="Chunk not found")
    return chunk


@router.put("/{chunk_id}", response_model=Chunk)
def update_chunk(chunk_id: str, updated_chunk: Chunk):
    """
    Update a chunk by id
    """
    chunk = chunk_service.update_chunk(chunk_id, updated_chunk)
    if not chunk:
        raise HTTPException(status_code=404, detail="Chunk not found")
    return chunk


@router.delete("/{chunk_id}", response_model=Chunk)
def delete_chunk(chunk_id: str):
    """
    Delete a chunk by id
    """
    chunk = chunk_service.delete_chunk(chunk_id)
    if not chunk:
        raise HTTPException(status_code=404, detail="Chunk not found")
    return chunk
