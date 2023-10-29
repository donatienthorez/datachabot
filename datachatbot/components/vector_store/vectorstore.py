import os
import shutil

from langchain.vectorstores import FAISS
from components.embeddings import Embeddings
from langchain.schema.document import Document
from utils.file_manager import FileManager
from typing import (List)

VECTOR_STORE_FOLDER = "faiss_vector_db"

class VectorStore:
    def __init__(self, embeddings: Embeddings, file_manager: FileManager):
        self.embeddings = embeddings
        self.file_manager = file_manager

    def create(self, chunks: List[Document]):
        vectorstore = FAISS.from_documents(documents = chunks, embedding=self.embeddings)
        vectorstore.save_local(VECTOR_STORE_FOLDER)

    def load(self):
        return FAISS.load_local(VECTOR_STORE_FOLDER, embeddings=self.embeddings)
    
    def clear(self):
        self.file_manager.remove_folder(folder=VECTOR_STORE_FOLDER)

    def exists(self):
        return os.path.exists(VECTOR_STORE_FOLDER)
