
from dotenv import load_dotenv

from components.vector_store.vectorstore import VectorStore
from components.embeddings import Embeddings
from components.documents import Documents
from components.llm.open_ai_llm import OpenAILlM
from components.qa_model import QA_Model
from components.document_splitter import DocumentSplitter

from utils.file_manager import FileManager
from utils.formatter import Formatter

class ChatViewModel:
    def __init__(self):
        load_dotenv()
        llm = OpenAILlM()
        embeddings = Embeddings()
        self.file_manager = FileManager()
        vector_store = VectorStore(embeddings=embeddings.get(), file_manager=self.file_manager)
        self.qa_model= QA_Model(vector_store=vector_store, llm=llm)
        self.document_splitter = DocumentSplitter()
        self.documents = Documents(document_splitter=self.document_splitter, vector_store=vector_store)
        self.formatter = Formatter()

    def show_chat(self):
        return self.qa_model.vector_store.exists()
    
    def save_files(self, uploaded_files):
        self.file_manager.save_files(uploaded_files=uploaded_files)

    def ingest_docs(self):
        self.documents.ingest_docs()

    def clear_database(self):
        self.qa_model.vector_store.clear()
        self.file_manager.clear()

    def generate_response(self, prompt):
        response, sources = self.qa_model.generate_response(prompt)
        return f"""
                {response}    
                &mdash;   
                {Formatter.format_sources(sources)}
            """
    
