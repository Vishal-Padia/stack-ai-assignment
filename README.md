# stack-ai-assignment
Assignment provided by Antoni from Stack-AI

Link to the assignment: https://stack-ai.notion.site/Take-at-Home-Task-Backend-Vector-DB-bff06d35e031498fb6469875a40adeea

## Problem Statement:
The goal of this project is to develop a REST API that allows users to index and query their documents within a Vector Database. A Vector Database specializes in storing and indexing vector embeddings, enabling fast retrieval and similarity searches. This capability is crucial for applications involving natural language processing, recommendation systems, and more.

The REST API should be containerized in a Docker container and deployed in a standalone Kubernetes cluster (no need to have more than one db node).

## Definitions:

To ensure a clear understanding, let's define some key concepts:

1. Chunk: A chunk is a piece of text with an associated embedding and metadata.
2. Document: A document is made out of multiple chunks, it also contains metadata.
3. Library: A library is made out of a list of documents and can also contain other metadata.

## This is what API should do:

1. Allow the users to create, read, update, and delete libraries.
2. Allow the users to create, read, update and delete chunks within a library.
3. Index the contents of a library.
4. Do k-Nearest Neighbor vector search over the selected library with a given embedding query.

## Guidelines:

1. Define the chunnk, document and Library classes. To simplify schema defintion use a fixed schema for all the classes. This means not letting the user define which fields should be present within the metadata for each class. 
2. Implement two or three indexing algorithms, do not use external libraries for this. Also what is the complexity of the indexing algorithm? why did you choose this algorithm?
3. Implement the necessary data structures/algorithms to ensure that there are no data races betweeen reads and write to the database. Explain the design choices.
4. Create the logic to do the CRUD operations on libraries and documents/chunk. Ensure data consistency and integrity during these operations.
5. Implement an API layer on top of that logic to let users interact with the vector database.
6. Create a docke image for the project and a helmchart to install it ina kubernetes cluster like a minikube.

