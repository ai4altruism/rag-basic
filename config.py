# config.py
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()

class Config:
    def __init__(self):
        # Try to get API key from multiple sources
        self.openai_api_key = (
            os.getenv("OPENAI_API_KEY") or 
            st.secrets.get("OPENAI_API_KEY")  # In case using Streamlit secrets
        )
        
        if not self.openai_api_key:
            raise ValueError("OPENAI_API_KEY must be set in environment variables or Streamlit secrets")
            
        # Set OpenAI key in environment
        os.environ["OPENAI_API_KEY"] = self.openai_api_key
        
        # Other config values
        self.LANGUAGE_MODEL = os.getenv("LANGUAGE_MODEL", "gpt-4")
        self.LLM_MAX_TOKENS = int(os.getenv("LLM_MAX_TOKENS", "4096"))
        self.LLM_TEMPERATURE = float(os.getenv("LLM_TEMPERATURE", "0.7"))
        self.VECTOR_STORE_PATH = os.getenv("VECTOR_STORE_PATH", "./vectorstore")