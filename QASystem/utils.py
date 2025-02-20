from haystack_integrations.document_stores.pinecone import PineconeDocumentStore

import os 
from dotenv import load_dotenv

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

# setting env variable 
os.environ['PINECONE_API_KEY'] = PINECONE_API_KEY

print("import Successfully")

