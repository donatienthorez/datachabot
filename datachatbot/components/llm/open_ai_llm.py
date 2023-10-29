from dotenv import load_dotenv
from langchain.llms import OpenAI
from components.llm.llm import Llm
import os

class OpenAILlM(Llm):
    def __init__(self):
        self.llm = OpenAI(
            model="text-davinci-003",
            openai_api_key=os.environ['OPEN_AI_API_TOKEN'],
            temperature=0)

    def get(self):
        return self.llm