from haystack import Pipeline 
from haystack.components.writers import DocumentWriter
from haystack.components.splitters import DocumentSplitter
from haystack.components.preprocessors import SentenceTransformersDocumentEmbedder
from haystack_integrations.document_store.pinecone import PineconeDocumentStore
from haystack.components.converters import PyPDFToDocument  # Fixed import path
from pathlib import Path  # Fixed incorrect import
import os 
from dotenv import load_dotenv 
from QASystem.utils import pinecone_config  # Assuming this is correct


def ingest():

    pass 


if __name__ == "__main__":
    ingest()


