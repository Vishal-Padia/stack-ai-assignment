from typing import List, Optional
from src.core.models.document import Document


class DocumentService:
    def __init__(self):
        self.documents: List[Document] = []

    def create_document(self, document: Document) -> Document:
        """
        Create a new Document
        """
        self.documents.append(document)
        return document

    def get_document(self, document_id: str) -> Optional[Document]:
        """
        Get a Document by ID
        """
        return next((doc for doc in self.documents if doc.id == document_id), None)

    def update_document(
        self, document_id: str, updated_document: Document
    ) -> Optional[Document]:
        """
        Update a document by it's ID
        """
        for i, doc in enumerate(self.documents):
            if doc.id == document_id:
                self.documents[i] = updated_document
                return updated_document
        return None

    def delete_document(self, document_id: str) -> bool:
        """
        Delete a document by it's ID
        """
        for i, doc in enumerate(self.documents):
            if doc.id == document_id:
                del self.documents[i]
                return True
        return False
