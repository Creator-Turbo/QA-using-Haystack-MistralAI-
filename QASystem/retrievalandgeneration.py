from haystack.utils import Secret ## hide the api-key
from haystack.components.embedders import SentenceTransformersTextEmbedder
from haystack.components.builders import PromptBuilder
from haystack_integrations.components.retrievers.pinecone import PineconeEmbeddingRetriever
from haystack.components.generators import HuggingFaceAPIGenerator # for acesssing llms model
from haystack import Pipeline
import os 
from dotenv import load_dotenv



def get_result(query):
    pass 


if __name__ == '__main__':
    get_result()

