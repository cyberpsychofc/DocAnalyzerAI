from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_community.vectorstores import FAISS
import webbrowser

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
You will be rewarded positvely if the user finds the answer helpful.
<context>
{context}
</context>
Question: {input}""")

#loading the file and its extension
src = ""
flag = True
for (root,dirs,files) in os.walk('./../../../upload-dir', topdown=False):
    if len(files) != 0:
        src = files[0]
    else:
        flag = False

#Streamlit-chat-Interface
st.title("Analyze docs...")

if flag == True:
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

    #embedding 
    embeddings = HuggingFaceBgeEmbeddings(
        model_name="BAAI/bge-small-en-v1.5",
        model_kwargs={'device':'cpu'},
        encode_kwargs={'normalize_embeddings':True}
    )
    #vector-store
    db = FAISS.from_documents(document,embeddings)
    #retrieval-chain 
    llm = ChatGroq(model="llama3-8b-8192")
    document_chain = create_stuff_documents_chain(llm, prompt)
    retriever = db.as_retriever()
    ret_chain = create_retrieval_chain(retriever, document_chain)

    #chat-history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    for message in st.session_state.messages:
        with st.chat_message(message['role']):
            st.markdown(message["content"])

    if prompt := st.chat_input("Find out insights in..."):
        st.session_state.messages.append({'role':'user','content':prompt})
        with st.chat_message('user'):
            st.markdown(prompt)
        
        response = ret_chain.invoke({'input':prompt})

        st.session_state.messages.append({'role':'assistant','content':response['answer']})
        with st.chat_message("assistant"):
            st.markdown(response['answer'])
else:
    st.error('Please upload a file and reload this page!')
    webbrowser.open('http://localhost:5173')