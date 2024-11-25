AI Agent for PDF Document Question-Answering
This project implements an AI agent that leverages the capabilities of a large language model to extract answers based on the content of a large PDF document. The AI agent uses OpenAI LLMs and is implemented using the Langchain frameworks for document parsing and question-answering functionality.

Project Structure
plaintext
Copy code
project-folder/
│
├── app.py                  # Streamlit app for user interface
├── requirements.txt        # List of dependencies
├── .env                    # Environment variables (API keys, config)
│
└── services/               # Contains core service implementations
    ├── chroma_client.py    # Client for managing ChromaDB
    ├── model_wrapper.py    # Wrapper for interacting with OpenAI LLM
    ├── pdf_parser.py       # PDF content extraction and parsing
    └── qa_agent.py         # Main question-answering agent logic
Description of Files
app.py: The entry point for the application. It uses Streamlit to provide a UI where users can upload PDFs and ask questions. This file orchestrates the interaction between different services and displays answers based on the model's responses.

requirements.txt: Contains all the necessary Python packages for the application, such as Streamlit, OpenAI SDK, Langchain, and others.

.env: This file holds sensitive environment variables like the OpenAI API key, paths for ChromaDB, and the embedding model identifier. These variables should not be shared or version-controlled.

services/:

chroma_client.py: Manages the connection and interactions with ChromaDB for storing and retrieving embeddings.
model_wrapper.py: A wrapper for OpenAI LLM to handle query processing and responses.
pdf_parser.py: Contains the logic to parse and extract text content from PDF files, which is then used for embedding and further processing.
qa_agent.py: The main component that manages the question-answering logic, integrating the PDF parsing, embeddings, and querying the model.
Installation
Prerequisites
Python 3.7 or higher
An OpenAI API key (sign up at OpenAI to get your key)
ChromaDB installed (used for document storage and querying embeddings)
Step 1: Clone the repository

git clone <repository-url>
cd <project-folder>
Step 2: Create a virtual environment (optional but recommended)

python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Step 3: Install dependencies

pip install -r requirements.txt
Step 4: Set up the .env file
Create a .env file in the root directory of your project. This file should contain the following environment variables:

plaintext
Copy code
OPENAI_API_KEY=your-openai-api-key
CHROMADB_PATH=path-to-your-chroma-db
EMBEDDING_MODEL=text-embedding-ada-002  # Or any OpenAI embedding model
Step 5: Run the application
To start the app, use the following command:


streamlit run app.py
How It Works
PDF Upload: The user uploads a PDF document via the Streamlit interface.
PDF Parsing: The content of the PDF is extracted using the pdf_parser.py service.
Embedding Generation: The extracted text is then transformed into embeddings using the chroma_client.py and stored in ChromaDB.
Question-Answering: The user asks a question related to the document. The question is passed to the qa_agent.py, which retrieves relevant embeddings from ChromaDB, queries the OpenAI LLM, and returns the answer.
Result Display: The answer is displayed back to the user via the Streamlit interface.
Code Explanation
app.py
This is the main file that sets up the Streamlit interface and integrates the core logic from the services. It allows users to upload a PDF and ask questions.

services/chroma_client.py
This file manages the connection with ChromaDB, responsible for storing and retrieving document embeddings. It provides functionality to save embeddings and fetch similar ones based on the user's query.

services/model_wrapper.py
The model_wrapper.py wraps the OpenAI model. It provides methods for interacting with the OpenAI API to send queries and receive responses based on embeddings.

services/pdf_parser.py
This service is responsible for parsing PDF files and extracting text. It uses libraries like PyPDF2 or pdfplumber to process the PDFs and output the text.

services/qa_agent.py
The qa_agent.py coordinates the overall question-answering process. It integrates the PDF parser and ChromaDB client to handle the embedding-based question-answering.