from dotenv import load_dotenv
from langchain.chains import RetrievalQA

from components.vector_store.vectorstore import VectorStore
from components.llm.llm import Llm

class QA_Model:
    def __init__(self, vector_store: VectorStore, llm: Llm):
        self.vector_store = vector_store
        self.llm = llm

    def generate_response(self, user_input):
        retrievalQA = RetrievalQA.from_chain_type(
                llm=self.llm.get(), 
                chain_type="stuff",
                retriever=self.vector_store.load().as_retriever(search_kwargs={"k": 2}),
                return_source_documents=True
            )

        result = retrievalQA(user_input)
        return result["result"], result["source_documents"]

