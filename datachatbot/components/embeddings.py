from langchain.embeddings import HuggingFaceEmbeddings

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

class Embeddings:

    def __init__(self):
        self.llm = HuggingFaceEmbeddings(model_name=MODEL_NAME)

    def get(self):
        return self.llm
