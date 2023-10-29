import streamlit as st
import os
from components.qa_model import QA_Model

from utils import Utils

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
            message_placeholder = st.empty()
            response, sources = qa_model.generate_response(prompt)

            finalResponse = Utils.format_response(response = response, sources= sources)
            message_placeholder.markdown(finalResponse)
            st.session_state.messages.append({"role": "assistant", "content": finalResponse})

def create_setup():
    st.title("Data Chatbot")
    
    uploaded_files = st.file_uploader("Please upload your PDF files", type="pdf")
    
    if st.button("Process", type="primary"):
        documents = []

        # for uploaded_file in uploaded_files:
        #     # Get the full file path of the uploaded file
        #     file_path = os.path.join(os.getcwd(), uploaded_file.name)

        #     # Save the uploaded file to disk
        #     with open(file_path, "wb") as f:
        #         f.write(uploaded_file.getvalue())

        #     # Use UnstructuredFileLoader to load the PDF file
        #     loader = UnstructuredFileLoader(file_path)
        #     loaded_documents = loader.load()
        #     print(f"Number of files loaded: {len(loaded_documents)}")

        #     # Extend the main documents list with the loaded documents
        #     documents.extend(loaded_documents)