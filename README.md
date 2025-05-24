# Generative AI-Powered QA System for UNIVESP Academic Programs

## Overview

This is a personal project built with Python, leveraging the LangChain and FAISS (Facebook AI Similarity Search) libraries. The tool is designed as a backend system to help users easily search and retrieve technical information from the curriculum documents of UNIVESP, a Brazilian public university offering Bachelor’s degree programs in Information Technology, Data Science, and Computer Engineering.

### Key Components

1. **Embedding Creation (OpenAI API):**

- Imports curriculum documents.
- Generates embeddings using the OpenAI API.
- Creates the vector store and saves it locally to avoid redundant processing.
- This process is performed only once; after creation, the vector store can be directly consumed in `main.py`.
- Script: `embedding_creator.py`.

2. **Information Retrieval:**

- Provides a function to send user queries to the RetrievalQA chain and obtain responses.
- Handles response output by printing the question and the retrieved answer in a user-friendly format.
- Includes basic exception handling to capture and display potential errors during retrieval.
- Script: `retrieval.py`.

3. **User Query Processing (OpenAI GPT-4o):**

- Defines the LLM (GPT-4o) from OpenAI.
- Loads the pre-created vector store for efficient retrieval.
- Uses the retrieval function to perform searches and return results.
- Script: `main.py`.
<!--
### Technologies Used
- Python
- LangChain
- FAISS
<!-- Add more here if necessary, e.g., FastAPI, Pandas... -->

## How to Use

1. **Clone the repository:**
   
   ```bash
   git clone https://github.com/sbitencourt/rag-pedagogical-qa.git
   cd rag-pedagogical-qa.git)
   ```

2. **(Optional but recommended) Create and activate a virtual environment:**

   - On macOS/Linux:
     
     ```bash
     python -m venv venv
     source venv/bin/activate
     ```

   - On Windows:
  
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   
3. **Install pre-requisite packages:**
   
   ```bash
   python -m pip install -r requirements.txt
   ```

4. **Set up your environment variables:**
   
   Create a .env file in the root directory of the project and add your OpenAI API key:
   ```bash
   OPENAI_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
   ```
  
5. **Run the application:**

     ```bash
     python main.py
     ```
