import streamlit as st
import os
from components.qa_model import QA_Model

from utils import Utils
from ingest import ingest_docs

def create_application(qa_model: QA_Model):
    if not qa_model.vector_store.exists():
        st.session_state.show_setup_screen = True

    if "show_setup_screen" in st.session_state:
        create_setup()
    else:
        create_chat(qa_model=qa_model)

def create_chat(qa_model: QA_Model):
    st.title("Data Chatbot")

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input("What is up?"):

        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            message_placeholder = st.markdown("AI is thinking...")
            response, sources = qa_model.generate_response(prompt)

            finalResponse = Utils.format_response(response = response, sources= sources)
            message_placeholder.markdown(finalResponse)
            st.session_state.messages.append({"role": "assistant", "content": finalResponse})

def create_setup():
    st.title("Data Chatbot Setup")

    st.info("No database was found. Please add any files you want to constitute the database. Once done, click on Process")
    
    uploaded_files = st.file_uploader("Please upload your PDF files", type="pdf", accept_multiple_files=True)
    
    if st.button("Process", type="primary"):
        documents = []
        
        with st.spinner('Moving your files into docs folder'):
            if not os.path.exists("./docs"):
                os.makedirs("./docs")
            
            for file in uploaded_files:
                if file:
                    with open(os.path.join("./docs", file.name), "wb") as f:
                        f.write(file.read())
                    documents.append(file.name)
        with st.spinner('Ingesting documents...'):
            ingest_docs()
            del st.session_state.show_setup_screen
            st.rerun()
