from dotenv import load_dotenv
from components.vectorstore import VectorStore
from components.embeddings import Embeddings
from components.document_splitter import DocumentSplitter

def ingest_docs():
    embeddings = Embeddings()
    vectorStore = VectorStore(embeddings=embeddings.get())
    chunks = DocumentSplitter().create_chunks()

    vectorStore.create(chunks=chunks)

def main():
    load_dotenv()
    ingest_docs()
    print("Success! Your data has been ingested!")

if __name__ == "__main__":
    main()
