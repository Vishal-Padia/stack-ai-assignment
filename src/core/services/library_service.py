from typing import List, Optional
from src.core.models.library import Library


class LibraryService:
    def __init__(self):
        self.libraries: List[Library] = []

    def create_library(self, library: Library) -> Library:
        """
        Create a new Library
        """
        self.libraries.append(library)
        return library

    def get_library(self, library_id: str) -> Optional[Library]:
        """
        Get a Library by ID
        """
        return next((lib for lib in self.libraries if lib.id == library_id), None)

    def update_library(
        self, library_id: str, updated_library: Library
    ) -> Optional[Library]:
        """
        Update a library by it's ID
        """
        for i, lib in enumerate(self.libraries):
            if lib.id == library_id:
                self.libraries[i] = updated_library
                return updated_library
        return None

    def delete_library(self, library_id: str) -> bool:
        """
        Delete a library by it's ID
        """
        for i, lib in enumerate(self.libraries):
            if lib.id == library_id:
                del self.libraries[i]
                return True
        return False
