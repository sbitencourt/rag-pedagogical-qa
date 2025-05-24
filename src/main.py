# main.py

# Libraries
from langchain_openai import ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.chains import LLMChain
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain.chains.combine_documents.stuff import StuffDocumentsChain
import os
from dotenv import load_dotenv
from functions.retrieval import send_question  # <- Import the retriever function

# Load environment variables from .env file
load_dotenv()

# Choose the model
llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0.5,
    api_key=os.getenv("OPENAI_API_KEY")
)

# Choose the embedding model
embeddings = OpenAIEmbeddings()

# Load the saved FAISS index
vectorstore = FAISS.load_local("data/faiss_index", embeddings, allow_dangerous_deserialization=True)

# Create a question-answering (QA) chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vectorstore.as_retriever()
)

# Define the question in Portuguese
portuguese_question = """Quais ferramentas serão abordadas no programa?"""

# Call the send_question function
send_question(portuguese_question, qa_chain)
