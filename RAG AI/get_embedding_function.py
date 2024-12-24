from langchain_openai import OpenAIEmbeddings
import os
from dotenv import load_dotenv
import openai

# Load environment variables from .env file
load_dotenv()

# Load the API key from the environment variable
api_key = os.getenv("OPENAI_API_KEY")

if api_key is None:
    raise ValueError("API key is not set in environment variables.")

# Set the API key for OpenAI
openai.api_key = api_key

def get_embedding_function(model_type="openai"):
    """
    Returns the embedding function based on the specified model type.
    
    Parameters:
        model_type (str): Only "openai" is supported.
        
    Returns:
        embeddings (object): The OpenAI embedding function.
    """
    if model_type == "openai":
        # Use OpenAI embeddings (requires an API key to be set as an environment variable)
        embeddings = OpenAIEmbeddings()
    else:
        raise ValueError("Invalid model_type. Only 'openai' is supported.")
    
    return embeddings
