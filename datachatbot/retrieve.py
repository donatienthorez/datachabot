
from dotenv import load_dotenv
from langchain.llms import HuggingFaceHub
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA

def load():
    load_dotenv()
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector_store = FAISS.load_local("faiss_vector_db", embeddings= embeddings)
    repo_id = "tiiuae/falcon-7b-instruct"
    llm = HuggingFaceHub(
        repo_id=repo_id,
        model_kwargs={
            "temperature": 0.1,
            "max_new_tokens":100,
        },
    )

    return RetrievalQA.from_chain_type(
        llm=llm, 
        chain_type="stuff",
        retriever=vector_store.as_retriever(), 
        return_source_documents = True
    )

def generate_response(user_input, qa_model):
    result = qa_model(user_input)
    return result["result"], result["source_documents"]