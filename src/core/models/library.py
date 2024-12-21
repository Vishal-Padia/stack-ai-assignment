from pydantic import BaseModel, Field
from typing import List, Dict, Any
from .document import Document


class Library(BaseModel):
    id: str = Field(..., description="Unique identifier for the library")
    documents: List[Document] = Field(
        [], description="List of documents in the library"
    )
    metadata: Dict[str, Any] = Field(
        {}, description="Additional metadata for the library"
    )
