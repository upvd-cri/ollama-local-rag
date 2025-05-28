import argparse
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores import FAISS
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain_ollama import OllamaEmbeddings

FAISS_PATH = "faiss"

def main():
    # Create CLI.
    parser = argparse.ArgumentParser()
    parser.add_argument("query_text", type=str, help="The query text.")
    args = parser.parse_args()
    query_text = args.query_text

    # Initialize LLM
    llm = ChatOllama(model="llama3", temperature=0)

    # Initialize embedding model
    embeddings = OllamaEmbeddings(model="mxbai-embed-large")

    # Create vector object from local vector store
    vector = FAISS.load_local(FAISS_PATH, embeddings, allow_dangerous_deserialization=True)

    # Set up chain
    prompt = ChatPromptTemplate.from_template("""Réponds à la question suivante en vous basant uniquement sur le contexte fourni:

    <context>
    {context}
    </context>

    Question: {input}""")

    document_chain = create_stuff_documents_chain(llm, prompt)

    # Set up retiever
    retriever = vector.as_retriever()
    retrieval_chain = create_retrieval_chain(retriever, document_chain)

    # Invoke using RAG
    response = retrieval_chain.invoke({"input": query_text})
    print(response["answer"])


if __name__ == "__main__":
    main()