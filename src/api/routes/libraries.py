from fastapi import APIRouter, HTTPException
from src.core.models.library import Library
from src.core.services.library_service import LibraryService

router = APIRouter()
library_service = LibraryService()


@router.post("/")
def create_library(library: Library):
    """
    Create a new library
    """
    return library_service.create_library(library)


@router.get("/{library_id}", response_model=Library)
def get_library(library_id: str):
    """
    Get a library by id
    """
    library = library_service.get_library(library_id)
    if not library:
        raise HTTPException(status_code=404, detail="Library not found")
    return library


@router.put("/{library_id}", response_model=Library)
def update_library(library_id: str, library: Library):
    """
    Update a library by id
    """
    library = library_service.update_library(library_id, library)
    if not library:
        raise HTTPException(status_code=404, detail="Library not found")
    return library


@router.delete("/{library_id}", response_model=dict)
def delete_library(library_id: str):
    """
    Delete a library by id
    """
    if not library_service.delete_library(library_id):
        raise HTTPException(status_code=404, detail="Library not found")
    return {"message": "Library deleted successfully"}
