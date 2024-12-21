from fastapi import APIRouter, HTTPException
from src.core.models.document import Document
from src.core.services.document_service import DocumentService

router = APIRouter()
document_service = DocumentService()


@router.post("/", response_model=Document)
def create_document(document: Document):
    """
    Create a new document
    """
    return document_service.create_document(document)


@router.get("/{document_id}", response_model=Document)
def get_document(document_id: str):
    """
    Get a document by id
    """
    document = document_service.get_document(document_id)
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")
    return document


@router.put("/{document_id}", response_model=Document)
def update_document(document_id: str, updated_document: Document):
    """
    Update a document by id
    """
    document = document_service.update_document(document_id, updated_document)
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")
    return document


@router.delete("/{document_id}", response_model=Document)
def delete_document(document_id: str):
    """
    Delete a document by id
    """
    document = document_service.delete_document(document_id)
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")
    return document
