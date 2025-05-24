# Libraries
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.prompts import ChatPromptTemplate
from langchain.chains import SimpleSequentialChain
from langchain.chains import LLMChain
from langchain.chains import ConversationChain
from langchain.globals import set_debug
from langchain.memory import ConversationSummaryMemory
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
#from langchain.vectorstores import FAISS # deprecated
from langchain.chains import RetrievalQA
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai.embeddings import OpenAIEmbeddings
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
set_debug(True)

# Choose the model
llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0.5,
    api_key=os.getenv("OPENAI_API_KEY"))

# Load the PDF file
loader = PyPDFLoader("data/documents/2024PPC-BTI__1__Ciencias_de_dados.pdf")
documents = loader.load()

# Split the documents into chunks
text_splitter = CharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

# Choose the embedding model
embeddings = OpenAIEmbeddings()

# Create the vector store
vectorstore = FAISS.from_documents(
    documents,
    embeddings
)

# Salvar a base de dados vetorial para futuras buscas
vectorstore.save_local("data/faiss_index/")