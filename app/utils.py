import os
from langchain_community.document_loaders import DirectoryLoader, PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter


def load_documents(directory):
    """ load pdf documents from a directory """
    loader = DirectoryLoader(
        directory,
        glob="**/*.pdf",
        loader_cls=PyMuPDFLoader
    )
    documents = loader.load()
    return documents

def split_chunks(documents, chunk_size=1000, chunk_overlap=200):
    """ split documents into chunks """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )
    chunks = splitter.split_documents(documents)
    return chunks

def format_docs_for_prompt(docs):
    """ format and clean the documents for the prompt """
    formatted = []
    
    for _, (doc, score) in enumerate(docs):
        source = doc.metadata.get("source", "Unknown Source")
        book_name = os.path.basename(source)
        page = doc.metadata.get("page", "N/A")
        content = doc.page_content.strip()
        content = " ".join(content.split())
        content = content.replace("- ", "")
        chunk_id = doc.id
        
        format = (
            f"### Document: {chunk_id}\n"
            f"Source: {book_name}\n"
            f"Page: {page}\n"
            f"\nContent: {content}\n"
            f"{'---'}\n"
        )
        formatted.append(format)
    return "\n".join(formatted)
