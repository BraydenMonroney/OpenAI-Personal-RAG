# OpenAI-Personal-RAG
Create your personal RAG bot using OpenAI resources!

This is an Openai RAG bot that is linked to an Openai API. You can upload any pdf into your local data file as your database. You can query the database by using the command-  python query_data.py "..." and in the parentheses any question you like about the data. The response will give you an answer that is drawn directly from the pdfs, and will cite the information from each page. Firstly, clone the files into a local repository. Then if you haven’t already, download Ollama locally. Then run all of the commands below, and make sure that you start a local environment. Then acquire an Openai API key and pay a fee so that OpenAI can run the tasks for you. Then create a file called .env and put in it OPENAI_API_KEY=   followed by your personal key where it will store and mobilize the information.



python -m venv .venv
Pip install chromadb
Pip install pypdf
Pip install pytest
Pip install langchain
pip install langchain-community
pip install openai
pip install langchain_openai
