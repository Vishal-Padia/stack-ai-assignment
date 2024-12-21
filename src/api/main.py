from fastapi import FastAPI
from src.api.routes import libraries, documents, chunks

app = FastAPI()

# include the routes
app.include_router(libraries.router, prefix="/libraries", tags=["libraries"])
app.include_router(documents.router, prefix="/documents", tags=["documents"])
app.include_router(chunks.router, prefix="/chunks", tags=["chunks"])


@app.get("/")
def read_root():
    return {"message": "Welcome to the Vector Database API!"}
