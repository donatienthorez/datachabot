from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

CHUNK_SIZE = 1028
CHUNK_OVERLAP = 100

class DocumentSplitter:
    def create_chunks(self):
        print ("Loading documents...")
        loader = DirectoryLoader(
            path='./docs',
            glob="**/*",
            show_progress=False,
            use_multithreading=True
        )
        print ("Documents loaded")
        print ("Creating chunks...")
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size = CHUNK_SIZE,
            chunk_overlap = CHUNK_OVERLAP,
            length_function = len,
        )

        chunks = loader.load_and_split(
            text_splitter=text_splitter
        )
        print("Created", len(chunks), "chunks of data")
        return chunks
