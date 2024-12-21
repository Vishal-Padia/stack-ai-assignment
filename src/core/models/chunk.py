from pydantic import BaseModel, Field
from typing import Dict, Any


class Chunk(BaseModel):
    id: str = Field(..., discrption="Unique identifier of the chunk")
    text: str = Field(..., description="Text content of the chunk")
    embedding: list[float] = Field(..., description="The Vector Embedding of the chunk")
    metadata: Dict[str, Any] = Field({}, description="Additional metadata of the chunk")
