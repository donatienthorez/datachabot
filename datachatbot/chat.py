import streamlit as st

from components.qa_model import QA_Model
from components.documents import Documents
from chat_view_model import ChatViewModel

def create_application(view_model: ChatViewModel):
    if view_model.show_chat():
        st.session_state.show_chat = True

    if "show_chat" not in st.session_state:
        create_setup(view_model = view_model)
    else:
        create_chat(view_model = view_model)
        
def create_setup(view_model: ChatViewModel):
    st.title("Data Chatbot Setup")

    st.info("No database was found. Please add any files you want to constitute the database. Once done, click on Process")
    
    uploaded_files = st.file_uploader("Please upload your PDF files", type="pdf", accept_multiple_files=True)
    
    if st.button("Process", type="primary"):        
        with st.spinner('Moving your files into docs folder'):
            view_model.save_files(uploaded_files=uploaded_files)

        with st.spinner('Ingesting documents...'):
            view_model.ingest_docs()
            st.session_state.show_chat = True
            st.rerun()

def create_chat(view_model: ChatViewModel):
    st.title("Data Chatbot")

    with st.sidebar:
        st.info('Press this button if you want to clear the database', icon="ℹ️")
        if st.button("Clear database", type="primary"):
            view_model.clear_database()
            del st.session_state.show_chat
            st.rerun()

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input("What's your question?"):

        # Add user message to the chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)

        # Display assistant response
        with st.chat_message("assistant"):
            message_placeholder = st.markdown("AI is thinking...")
            response = view_model.generate_response(prompt)
            message_placeholder.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
