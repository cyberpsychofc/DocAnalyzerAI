from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_community.vectorstores import FAISS

import streamlit as st

import os
from dotenv import load_dotenv

load_dotenv()

os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")
os.environ["LANGCHAIN_TRACING"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

prompt = ChatPromptTemplate.from_template("""
Answer the user's query in a structured way. You are supposed to
obtain insights and highlights about the information from documents, compare numbers. 
Think step by step before providing a detailed answer.
You will be reward you positvely if the user finds the answer helpful.
<context>
{context}
</context>
Question: {input}""")

#loading the file and its extension
src = ""
for (root,dirs,files) in os.walk('./../../../upload-dir', topdown=False):
    src = files[0]
file_path = './../../../upload-dir/data.'
extension = src[(len(src) - 3):]

#data-ingestion
loader = None

if extension == "txt":
    loader = TextLoader(file_path + extension)
if extension == "pdf":
    loader = PyPDFLoader(file_path + extension)

doc = loader.load()
doc_splitter = RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
document = doc_splitter.split_documents(doc)

#embedding to be done