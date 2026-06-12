import chromadb
from pathlib import Path
from parser import process_md
import json

DATABASE_URI = DATA_DIR = Path(__file__).parents[1] / 'data/chroma_db'
croma_client = chromadb.PersistentClient(path=DATABASE_URI)

collection = croma_client.get_or_create_collection(name="docs")

def vectorize_chunks():
    chunks = process_md()
    if not chunks: 
        raise ValueError("No chunks found. Please run the parser.py script first.")
    
    for chunk in chunks:
        collection.add(
            ids=[chunk['id']],
            documents = [chunk['text']],
            metadatas = [chunk['metadata']]
        )
    print("✅ Local Vector Database successfully populated and committed to disk!")

def ensure_collection_exists():
    # Collection exists but may be empty
    if collection.count() == 0:
        print("No documents found. Creating embeddings...")
        vectorize_chunks()
    else:
        print(f"Collection already populated ({collection.count()} docs).")

def query_local_database(prompt: str, num_results: int = 3):
    print(f"\nPrompt: '{prompt}'")
    results = collection.query(
        query_texts=[prompt],
        n_results=num_results
    )
    
    print(json.dumps(results, indent=2))

if __name__ == "__main__":
    ensure_collection_exists()
    
    query_local_database("what is chunking?", num_results=3)