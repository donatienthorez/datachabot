import os
import shutil

from langchain.vectorstores import FAISS
from components.embeddings import Embeddings
from langchain.schema.document import Document
from typing import (List)

VECTOR_STORE_FOLDER = "faiss_vector_db"

class VectorStore:

    def __init__(self, embeddings: Embeddings):
        self.embeddings = embeddings

    def create(self, chunks: List[Document]):
        vectorstore = FAISS.from_documents(documents = chunks, embedding=self.embeddings)
        vectorstore.save_local(VECTOR_STORE_FOLDER)

    def load(self):
        return FAISS.load_local(VECTOR_STORE_FOLDER, embeddings=self.embeddings)
    
    def clear(self):
        try:
            shutil.rmtree(VECTOR_STORE_FOLDER)
            print(f"Folder '{VECTOR_STORE_FOLDER}' has been successfully deleted.")
        except FileNotFoundError:
            print(f"Folder '{VECTOR_STORE_FOLDER}' not found.")
        except PermissionError:
            print(f"You do not have permission to delete '{VECTOR_STORE_FOLDER}'.")

    def exists(self):
        return os.path.exists(VECTOR_STORE_FOLDER)
