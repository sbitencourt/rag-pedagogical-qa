# send_question.py

# Libraries
from langchain.chains import RetrievalQA

def send_question(question, qa_chain):

    try:
        response = qa_chain.invoke({ "query" : question})
        print(f"\n🤷 Question: {question}")
        print("👾 Answer:")
        print(response['result'])

    except Exception as e:
        print(f"❌ Error: {e}")
