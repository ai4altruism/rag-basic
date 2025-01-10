# Basic RAG Pipeline

A simple Retrieval Augmented Generation (RAG) implementation using OpenAI, ChromaDB, and Streamlit. This version was developed with the assistance of Claude Sonnet 3.5.

## Overview

This project implements a basic RAG pipeline that allows users to:

- Upload text documents to a knowledge base
- Query the knowledge base using natural language
- Receive AI-generated responses based on the context of uploaded documents

## Technical Stack

- OpenAI API for embeddings and chat completion
- ChromaDB for vector storage
- Streamlit for web interface
- Python dotenv for configuration

## Prerequisites

- Python 3.8 or higher
- OpenAI API key
- Sufficient disk space for vector storage

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/rag-basic.git
cd rag-basic
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root with your configuration:

```bash
OPENAI_API_KEY=your_api_key_here
LANGUAGE_MODEL=gpt-4-1106-preview
LLM_MAX_TOKENS=4096
LLM_TEMPERATURE=0.7
VECTOR_STORE_PATH=./vectorstore
```

## Usage

1. Start the application:

```bash
streamlit run app.py
```

2. Open your web browser and navigate to the URL shown in the console (typically http://localhost:8501)

3. Use the interface to:
   - Upload text documents
   - Ask questions about the uploaded content
   - View AI-generated responses

## Project Structure

```
rag-basic/
├── .env                 # Configuration file
├── requirements.txt     # Project dependencies
├── config.py           # Configuration management
├── rag_pipeline.py     # Core RAG implementation
├── app.py              # Streamlit web interface
└── vectorstore/        # Directory for ChromaDB storage
```

## Limitations

- Currently supports only text (.txt) files
- Limited to specific versions of dependencies due to compatibility issues:
  - httpx==0.24.1
  - openai==1.6.1
  - chromadb==0.4.22
  - python-dotenv==1.0.0
  - streamlit==1.31.1

## Contributing

Feel free to open issues or submit pull requests with improvements.

## License

This project is licensed under the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html).
