# Langchain RAG Project

This repository is forked from [pixegami/langchain-rag-tutorial]

This repository provides an example of implementing Retrieval-Augmented Generation (RAG) using LangChain and Ollama. The RAG approach combines the strengths of an LLM with a retrieval system (in this case, FAISS) to allow the model to access and incorporate external information during the generation process.

The application will load any Markdown documents in the `docs/` directory. 

Credit to [pixegami](https://github.com/pixegami/langchain-rag-tutorial) for the inspiration for this project.

## LangChain

[LangChain](https://github.com/langchain-ai/langchain) is a framework for developing applications with LLMs. It provides a modular and extensible approach to building applications, allowing you to combine different components (e.g., LLMs, retrieval systems, data sources) in a flexible manner.

## FAISS

[FAISS](https://github.com/facebookresearch/faiss) (Facebook AI Similarity Search) is a library for efficient similarity search and dense vector clustering. In this example, we use FAISS as the retrieval system to store and search through text data.

## Ollama

[Ollama](https://github.com/ollama/ollama) is a tool for running large language models locally. Supported models are listed [here](https://ollama.com/library).

## Getting Started

To get started with this example, follow these steps:

Install python dependencies:

```python
pip install -r requirements.txt
```

Start Ollama with a model of you choice:

```bash
ollama run llama3
```

>NOTE: This model needs to match the model referenced in the python code.

Create the FAISS database:

```python
python create_database.py
```

This script reads files from a directory (specified in the script) and creates a FAISS index.

Query the FAISS database.

```python
python query_data.py "What is LangChain?"
```

This script takes a query as input, uses the LangChain [retrieval](https://python.langchain.com/docs/modules/data_connection/) to retrieve relevant information from the FAISS database, and generates a response using an LLM (specified in the script).

## Adding Documents

To add additional documents just copy them to the `docs/` directory. The application can support formats other than Markdown but you may need to install additional python packages.
