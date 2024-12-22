import threading
from typing import List, Optional
from src.core.models.library import Library


class LibraryService:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(LibraryService, cls).__new__(cls, *args, **kwargs)
            cls._instance.__initialized = False
        return cls._instance

    def __init__(self):
        if self.__initialized:
            return
        self.__initialized = True
        self.libraries: List[Library] = []
        self.lock = threading.Lock()  # Exclusive lock for write
        self.read_lock = threading.Lock()  # Shared locks for reads
        self.read_count = 0  # Track the number of readers

    def acquire_read_lock(self):
        """
        Acquire the read lock
        """
        self.read_lock.acquire()
        self.read_count += 1
        if self.read_count == 1:
            self.lock.acquire()  # block writes if this is first reader
        self.read_lock.release()

    def release_read_lock(self):
        """
        Release the read lock
        """
        self.read_lock.acquire()
        self.read_count -= 1
        if self.read_count == 0:
            self.lock.release()
        self.read_lock.release()

    def acquire_write_lock(self):
        """
        Acquire the write lock
        """
        self.lock.acquire()

    def release_write_lock(self):
        """
        Release the write lock
        """
        self.lock.release()

    def create_library(self, library: Library) -> Library:
        """
        Create a new Library
        """
        self.acquire_write_lock()
        try:
            self.libraries.append(library)
            print(f"Library created: {library.id}")  # Debug log
            print(
                f"Current libraries: {[lib.id for lib in self.libraries]}"
            )  # Debug log
            return library
        finally:
            self.release_write_lock()

    def get_library(self, library_id: str) -> Optional[Library]:
        """
        Get a Library by ID
        """
        self.acquire_read_lock()
        try:
            library = next(
                (lib for lib in self.libraries if lib.id == library_id), None
            )
            if library:
                print(f"Library found: {library.id}")
            else:
                print(f"Library not found: {library_id}")
            print(f"Current libraries: {[lib.id for lib in self.libraries]}")
            return library
        finally:
            self.release_read_lock()

    def update_library(
        self, library_id: str, updated_library: Library
    ) -> Optional[Library]:
        """
        Update a library by it's ID
        """
        self.acquire_write_lock()
        try:
            for i, lib in enumerate(self.libraries):
                if lib.id == library_id:
                    self.libraries[i] = updated_library
                    return updated_library
            return None
        finally:
            self.release_write_lock()

    def delete_library(self, library_id: str) -> bool:
        """
        Delete a library by it's ID
        """
        self.acquire_write_lock()
        try:
            for i, lib in enumerate(self.libraries):
                if lib.id == library_id:
                    del self.libraries[i]
                    return True
            return False
        finally:
            self.release_write_lock()
