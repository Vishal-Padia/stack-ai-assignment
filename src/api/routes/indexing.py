from fastapi import APIRouter, HTTPException, Body
from src.core.models.library import Library
from src.core.services.library_service import LibraryService
from src.core.indexing.algorithms.linear_search import LinearSearch
from src.core.indexing.algorithms.kd_tree import KDTreeIndex
from src.core.indexing.algorithms.ball_tree import BallTreeIndex

router = APIRouter()
library_service = LibraryService()

# Available indexing algorithms
INDEXING_ALGORITHMS = {
    "linear_search": LinearSearch,
    "kd_tree": KDTreeIndex,
    "ball_tree": BallTreeIndex,
}


@router.post("/index/{library_id}", response_model=dict)
def index_library(library_id: str, algorithm: str = "linear_search"):
    """
    Index the chunks in a library using the specified algorithm.
    """
    print(f"Indexing library: {library_id} with algorithm: {algorithm}")
    print(
        f"Current libraries before indexing: {[lib.id for lib in library_service.libraries]}"
    )

    # fetch the library
    library = library_service.get_library(library_id)
    if not library:
        raise HTTPException(status_code=404, detail=f"Library not found {library_id}")

    # extract chunks and their embeddingss
    data = []
    for document in library.documents:
        for chunk in document.chunks:
            data.append((chunk.id, chunk.embedding))

    # build the index
    if algorithm not in INDEXING_ALGORITHMS:
        raise HTTPException(
            status_code=400, detail=f"Invalid Indexing Algorithm: {algorithm}"
        )

    index_class = INDEXING_ALGORITHMS[algorithm]
    index = index_class()
    index.build_index(data)

    # store the index in library
    library.index = index
    print(f"Library indexed successfully: {library_id}")  # Debug log
    print(
        f"Current libraries after indexing: {[lib.id for lib in library_service.libraries]}"
    )  # Debug log

    # # store the index in the library service (for simplicity, we'll store it as an attribute)
    # library_service.libraries[library_service.libraries.index(library)].index = index

    return {"message": f"Library {library_id} indexed using {algorithm}"}


@router.post("/search/{library_id}", response_model=dict)
def search_library(
    library_id: str,
    query_embedding: list = Body(
        ..., description="The query embedding as a list of floats"
    ),
    k: int = Body(5, description="The number of nearest neighbors to return"),
):
    """
    Search for the k-nearest neighbors in the indexed library.
    """
    print(
        f"Searching library: {library_id} with query_embedding: {query_embedding} and k: {k}"
    )  # Debug log
    # fetch the library
    library = library_service.get_library(library_id)
    if not library:
        print(f"Library not found: {library_id}")  # Debug log
        raise HTTPException(status_code=404, detail="Library not found")

    if not library.index:
        print(f"Library is not indexed: {library_id}")  # Debug log
        raise HTTPException(status_code=400, detail="Library not indexed")

    # perform the search
    results = library.index.search(query_embedding, k)
    print(f"Search results: {results}")  # Debug log
    return {"results": results}
