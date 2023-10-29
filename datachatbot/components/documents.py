
from components.vector_store.vectorstore import VectorStore
from components.embeddings import Embeddings
from components.document_splitter import DocumentSplitter
from utils.file_manager import FileManager

class Documents:
    def __init__(self, document_splitter: DocumentSplitter, vector_store: VectorStore):
        self.document_splitter = document_splitter
        self.vector_store = vector_store

    def ingest_docs(self):
        chunks = self.document_splitter.create_chunks()
        self.vector_store.create(chunks=chunks)

    def clear(self):
        FileManager.clear()
