from dotenv import load_dotenv

from components.vectorstore import VectorStore
from components.embeddings import Embeddings
from components.llm import Llm
from components.qa_model import QA_Model

from chat import create_chat, create_setup

def main():
    load_dotenv()
    llm = Llm()
    embeddings = Embeddings()
    vector_store = VectorStore(embeddings=embeddings.get())
    qa_model = QA_Model(vector_store=vector_store, llm=llm)

    if vector_store.exists():
        create_chat(qa_model=qa_model)
    else:
        create_setup()


if __name__ == "__main__":
    main()