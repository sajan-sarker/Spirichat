from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from langchain_huggingface import HuggingFaceEmbeddings

from app.utils import load_documents, split_chunks
from app.config import *

import warnings 
warnings.filterwarnings("ignore")

def create_vector_store():
    """ Create a vector store using Pinecone and load documents into it. """
    # Load the documents from the specified directory
    print("Loading documents from the data directory...")
    data = load_documents("data/")

    # Split the documents into chunks
    chunks = split_chunks(data)

    # Initialize the HuggingFace embeddings
    print("Initializing HuggingFace embeddings...")
    embedding = HuggingFaceEmbeddings(
        model_name=os.getenv("EMBEDDING_MODEL_NAME"),
    )

    # Initialize the Pinecone vector store
    print("Connecting to Pinecone...")
    pinecone = Pinecone(
        api_key=os.getenv("PINECONE_API_KEY"),
    )
    index_name = os.getenv("PINECONE_INDEX_NAME")

    # Check if the index exists, if not exists, create it
    if not pinecone.has_index(index_name):
        pinecone.create_index(
            name=index_name,
            dimension=len(embedding.embed_query("Hello, world!")),
            metric="cosine",
            spec=ServerlessSpec(
                cloud="aws",
                region='us-east-1'
            )
        )
        print("Pinecone index created successfully.")
    else:
        print("Pinecone index already exists.")

    print("Creating the Pinecone vector store...")
    PineconeVectorStore.from_documents(
        documents=chunks,
        embedding=embedding,
        index_name=index_name
    )

    print("Vector store created and documents added successfully.")

if __name__ == "__main__":
    create_vector_store()
    print("\nKnowledge base initialized successfully.")