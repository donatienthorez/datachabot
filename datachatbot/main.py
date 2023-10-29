import streamlit as st

from chat import create_application
from chat_view_model import ChatViewModel

def main():
    chat_view_model = ChatViewModel()
    create_application(view_model=chat_view_model)

if __name__ == "__main__":
    main()