import os
from openai import OpenAI
import chromadb
from typing import List
import logging
import uuid

class RAGPipeline:
    def __init__(self, config):
        self.config = config
        self.client = OpenAI()
        
        # Initialize Chroma
        self.chroma_client = chromadb.PersistentClient(path=config.VECTOR_STORE_PATH)
        self.collection = self.chroma_client.get_or_create_collection(
            name="document_collection"
        )
    
    def embed_text(self, text: str) -> List[float]:
        """Generate embeddings for a single text."""
        response = self.client.embeddings.create(
            model="text-embedding-3-small",
            input=text
        )
        return response.data[0].embedding
    
    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        """Generate embeddings for a list of texts."""
        response = self.client.embeddings.create(
            model="text-embedding-3-small",
            input=texts
        )
        return [item.embedding for item in response.data]

    def add_documents(self, documents: List[str]):
        '''Add new documents to the vector store'''
        try:
            vectors = self.embed_documents(documents)
            
            # Generate unique IDs using UUID
            doc_ids = [str(uuid.uuid4()) for _ in documents]
            
            self.collection.add(
                embeddings=vectors,
                documents=documents,
                ids=doc_ids
            )
        except Exception as e:
            logging.error(f"Error adding documents: {str(e)}")
            raise
    
    def query(self, question: str) -> str:
        '''Query the RAG pipeline'''
        try:
            question_embedding = self.embed_text(question)
            
            # Get collection count
            collection_count = self.collection.count()
            n_results = min(2, collection_count)  # Adjust n_results based on available documents
            
            # Query Chroma
            results = self.collection.query(
                query_embeddings=[question_embedding],
                n_results=n_results
            ) if collection_count > 0 else {"documents": [[]]}
            
            context = " ".join(results['documents'][0]) if results['documents'] else ""
            
            messages = [
                {"role": "system", "content": "Use the provided context to answer the question. If the context doesn't contain the answer, say so."},
                {"role": "user", "content": f"Context: {context}\n\nQuestion: {question}"}
            ]
            
            response = self.client.chat.completions.create(
                model=self.config.LANGUAGE_MODEL,
                messages=messages,
                temperature=self.config.LLM_TEMPERATURE,
                max_tokens=self.config.LLM_MAX_TOKENS
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            logging.error(f"Error querying RAG pipeline: {str(e)}")
            return f"Error processing query: {str(e)}"