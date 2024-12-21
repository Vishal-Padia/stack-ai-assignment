from pydantic import BaseModel, Field
from typing import List, Dict, Any
from .chunk import Chunk


class Document(BaseModel):
    id: str = Field(..., description="Unique identifier for the document")
    chunks: List[Chunk] = Field([], description="List of chunks in the document")
    metadata: Dict[str, Any] = Field(
        {}, description="Additional metadata of the document"
    )
