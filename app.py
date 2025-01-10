import streamlit as st
from config import Config
from rag_pipeline import RAGPipeline
import logging

st.title("RAG Query Interface")

# Initialize RAG pipeline
config = Config()
rag = RAGPipeline(config)

# File upload with better handling
uploaded_file = st.file_uploader("Upload a document", type=['txt'])
if uploaded_file:
    try:
        # Try different encodings
        encodings = ['utf-8', 'latin-1', 'windows-1252']
        content = None
        
        for encoding in encodings:
            try:
                content = uploaded_file.read().decode(encoding)
                break
            except UnicodeDecodeError:
                uploaded_file.seek(0)  # Reset file pointer for next attempt
                continue
        
        if content:
            try:
                rag.add_documents([content])
                st.success("Document added to knowledge base!")
            except Exception as e:
                st.error(f"Error processing document: {str(e)}")
        else:
            st.error("Could not decode the file with any supported encoding.")
            
    except Exception as e:
        st.error(f"Error processing file: {str(e)}")

# Query interface
query = st.text_input("Enter your question:")
if query:
    response = rag.query(query)
    st.write("Response:", response)