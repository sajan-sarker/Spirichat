from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint, HuggingFaceEmbeddings
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from app.utils import *
from app.config import *
from app.prompt import prompt

def init_vector_store():
    """ Initialize the Pinecone vector store and return it. """
    # Initialize the HuggingFace embeddings
    embedding = HuggingFaceEmbeddings(
        model_name=os.getenv("EMBEDDING_MODEL_NAME"),
    )

    # Initialize the Pinecone vector store
    pinecone = Pinecone(
        api_key=os.getenv("PINECONE_API_KEY"),
    )

    # Connect to the Pinecone index
    index_name = os.getenv("PINECONE_INDEX_NAME")
    index = pinecone.Index(index_name)

    # Create the Pinecone vector store
    vector_store = PineconeVectorStore(
        index=index,
        embedding=embedding
    )

    return vector_store

def retrieve_query(query, top_k=5, get_k=3):
    """ Retrieve the top k documents from the vector store based on the query and return the top 3 results. """
    # Initialize the vector store
    vector_store = init_vector_store()

    # perform similarity search with score
    results = vector_store.similarity_search_with_score(
        query=query,
        k=top_k,
    )

    sorted_result = sorted(results, key=lambda x: x[1], reverse=True)   # Sort by score in descending order
    get3_docs = sorted_result[:get_k]   # Get top 3 documents and return them
    return get3_docs

def qa_chain():
    # Initialize the OpenAI chat model
    model = ChatOpenAI(
        model="gpt-3.5-turbo-0125",
        temperature=0.2,
        max_completion_tokens=200
    )

    # initialize the output parser
    # This parser will convert the model's output into a string format
    parser = StrOutputParser()

    # Define the parallel chain to run the retrieval and formatting in parallel
    # This chain will take the context and question as inputs and return the formatted query
    parallel_chain = RunnableParallel({
        "context": RunnableLambda(retrieve_query) | RunnableLambda(format_docs_for_prompt),
        "question": RunnablePassthrough()
    })

    # Combine the parallel chain with the prompt, model, and parser
    # This chain will first retrieve the context and format it, then use the prompt to create a query,
    # invoke the model with the query, and finally parse the output
    chain = parallel_chain | prompt | model | parser

    return chain
