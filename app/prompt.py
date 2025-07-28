from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate(
    template = """
    You are a helpful assistant for answering questions about Supernatural stuffs such as Ghost, Demon, Vampire, Werewolf, etc.

    Use the following context:
    ---------------
    {context}
    ---------------

    Answer the question concisely and accurately based on the provided context. If the answer is not in the context, say you don't know about this.
    Question: {question}
    Answer:
    """,
    input_variables=["context", "question"]
)