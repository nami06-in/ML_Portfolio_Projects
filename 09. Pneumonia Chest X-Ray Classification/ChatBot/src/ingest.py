import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_community.vectorstores import FAISS

from langchain_community.embeddings import HuggingFaceEmbeddings

from config import *

all_docs = []

for file in os.listdir(PDF_FOLDER):

    if file.endswith(".pdf"):

        pdf_path = os.path.join(PDF_FOLDER, file)

        loader = PyPDFLoader(pdf_path)

        docs = loader.load()

        all_docs.extend(docs)

print(f"Loaded {len(all_docs)} pages")

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_documents(all_docs)

print(f"Created {len(chunks)} chunks")

embeddings = HuggingFaceEmbeddings(
    model_name=EMBEDDING_MODEL
)

vector_db = FAISS.from_documents(
    chunks,
    embeddings
)

vector_db.save_local(VECTOR_DB_PATH)

print("FAISS database saved")