import os 
from langchain_community.embeddings import OpenAIEmbeddings
import chromadb
from dotenv import load_dotenv
import time
load_dotenv()
class ChromaClient:
    def __init__(self):
        # Initialize Chroma with local persistence
        storage_path = os.getenv("CHROMADB_PATH", "./chromadb")
        embedding_model_name = os.getenv("EMBEDDING_MODEL", "text-embedding-ada-002")
        self.persist_directory = storage_path
        self.collection_name = "pdf_chunks"
        self.embedding_model = OpenAIEmbeddings(model=embedding_model_name)
        
        self.client = chromadb.PersistentClient(path=storage_path)#Chroma(persist_directory=self.persist_directory, embedding_function=self.embedding_model)

    def store_chunks(self, chunks: list, metadata: list):
        """Stores chunks and their embeddings in Chroma."""
        collection = self.client.get_or_create_collection(self.collection_name)
        # Generate embeddings
        embeddings = self.embedding_model.embed_documents(chunks)
        # Generate unique IDs for chunks
        timestamp = str(int(time.time()))
        ids = [f"{self.collection_name}__{timestamp}_{str(i)}" for i in range(len(chunks))]
        # Add data to collection
        collection.add(
            documents=chunks,
            embeddings=embeddings,
            metadatas=metadata,
            ids=ids
        )
        print(f"Stored {len(chunks)} chunks in the collection '{self.collection_name}'.")

    def query_similar_chunks(self, query: str, top_k=5):
        """Retrieves top-k similar chunks based on query embedding."""
        collection = self.client.get_or_create_collection(self.collection_name)
        # Generate query embedding
        query_embedding = self.embedding_model.embed_query(query)
        # Perform query
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )
        return results['documents']

