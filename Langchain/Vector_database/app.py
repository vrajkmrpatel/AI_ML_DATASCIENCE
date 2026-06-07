import os
import streamlit as st
from uuid import uuid4

from dotenv import load_dotenv 
load_dotenv()

# LangChain & Pinecone Imports
from langchain_community.document_loaders import DirectoryLoader, PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore
from langchain_groq import ChatGroq
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

# ----------------------------------------------------
# 1. SECURE CREDENTIALS SETUP
# ----------------------------------------------------
# It's best practice to use Streamlit secrets or environment variables.
# You can set these in your terminal before running, or use a .env file.
# os.environ["PINECONE_API_KEY"] = "your-new-pinecone-key"
# os.environ["OPENAI_API_KEY"] = "your-openai-key"

# ----------------------------------------------------
# 2. CACHED RAG PIPELINE INITIALIZATION
# ----------------------------------------------------
@st.cache_resource
def initialize_rag_system():
    """Initializes the heavy components once and caches them to keep the UI fast."""
    
    # Initialize Embedding Model
    embeddings = HuggingFaceEmbeddings(model_name='BAAI/bge-large-en-v1.5')
    
    # Initialize Pinecone Index Connection
    pc = Pinecone(api_key=os.environ.get("PINECONE_API_KEY"))
    index_name = "langchainvector"
    index = pc.Index(index_name)
    
    # Initialize Vector Store
    vector_store = PineconeVectorStore(index=index, embedding=embeddings)
    
    # Initialize LLM
    llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0)
    
    # Build System Prompt Templates
    system_prompt = (
        "You are an expert financial analyst assistant. Use the provided pieces of retrieved context "
        "to answer the user's question with absolute precision.\n\n"
        "CRITICAL RULES:\n"
        "1. Pay close attention to document dates (e.g., 2024, 2025, 2026). Always state which report year you are pulling data from in your final answer.\n"
        "2. If values change across chunks, prioritize the most recent year's data unless asked otherwise.\n"
        "3. Keep formatting clean using bullet points for metrics.\n\n"
        "Context:\n{context}"
    )
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{input}"),
    ])
    
    # Assemble the final modern LangChain RAG Chain
    retriever = vector_store.as_retriever(search_kwargs={"k": 3})
    question_answer_chain = create_stuff_documents_chain(llm, prompt_template)
    rag_chain = create_retrieval_chain(retriever, question_answer_chain)
    
    return rag_chain

# Optional utility function if you need to upload new documents from the UI
def process_and_upload_docs(directory_path, _vector_store):
    """Loads, chunks, and pushes documents to your existing Pinecone index."""
    file_loader =  file_loader = DirectoryLoader(
        directory_path,
        glob="**/*.pdf", 
        loader_cls=PyMuPDFLoader,
    )
    docs = file_loader.load()
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
    chunked_docs = text_splitter.split_documents(docs)
    
    uuids = [str(uuid4()) for _ in range(len(chunked_docs))]
    _vector_store.add_documents(documents=chunked_docs, ids=uuids)
    return len(chunked_docs)


# ----------------------------------------------------
# 3. STREAMLIT UI LAYOUT
# ----------------------------------------------------
st.set_page_config(page_title="RAG Document Assistant", page_icon="🤖")
st.title("🤖 FinRAG")
st.subheader("Ask questions based on your knowledge base")

# Verify API Keys are available before proceeding
if not os.environ.get("PINECONE_API_KEY") or not os.environ.get("GROQ_API_KEY"):
    st.error("Missing API Keys! Please ensure PINECONE_API_KEY and GROQ_API_KEY are configured in your environment.")
    st.stop()

# Load the cached chain execution environment
try:
    rag_chain = initialize_rag_system()
except Exception as e:
    st.error(f"Failed to connect to Vector Store / LLM: {e}")
    st.stop()

# Initialize Chat History in Session State
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages on screen refresh
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle Chat Interactions
if user_query := st.chat_input("Ask a question about your documents..."):
    
    # 1. Display User Message
    st.session_state.messages.append({"role": "user", "content": user_query})
    with st.chat_message("user"):
        st.markdown(user_query)

    # 2. Generate and Display Response via RAG Chain
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        with st.spinner("Searching documents and thinking..."):
            try:
                # Fire the unified RAG chain
                response = rag_chain.invoke({"input": user_query})
                answer = response["answer"]
                response_placeholder.markdown(answer)
                
                # 3. Keep tracking history logs
                st.session_state.messages.append({"role": "assistant", "content": answer})
            except Exception as e:
                response_placeholder.error(f"An error occurred while generating a response: {e}")