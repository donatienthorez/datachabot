
from components.vectorstore import VectorStore
from components.embeddings import Embeddings

import os

def main():
    vectorStore = VectorStore(
        embeddings=Embeddings().get()
    ).clear()

if __name__ == "__main__":
    main()