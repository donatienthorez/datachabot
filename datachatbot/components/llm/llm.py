from dotenv import load_dotenv
from langchain.llms import HuggingFaceHub
from abc import ABC, abstractmethod

class Llm(ABC):

    @abstractmethod
    def get(self):
        pass
