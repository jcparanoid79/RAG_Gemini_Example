from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.prompts import PromptTemplate
import sys

# Agrega el directorio raíz del proyecto al sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Load environment variables from .env file
load_dotenv()

# Check for the API key
if "GOOGLE_API_KEY" not in os.environ:
    raise ValueError("GOOGLE_API_KEY not found in .env file.")
from langchain.chains import RetrievalQA

# Cargar los índices vectoriales
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

# Verificar si los índices existen
index_paths = ["faiss_index_tecnicos", "faiss_index_faqs", "faiss_index_comunicados"]
for path in index_paths:
    if not os.path.exists(path):
        print(f"Error: El índice '{path}' no se encuentra. Asegúrate de ejecutar 'ingestor.py' primero.")
        exit()

vectorstore_tecnicos = FAISS.load_local("faiss_index_tecnicos", embeddings, allow_dangerous_deserialization=True)
vectorstore_faqs = FAISS.load_local("faiss_index_faqs", embeddings, allow_dangerous_deserialization=True)
vectorstore_comunicados = FAISS.load_local("faiss_index_comunicados", embeddings, allow_dangerous_deserialization=True)

# Reemplazar ChatOpenAI por ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)

# Crear una cadena de RetrievalQA simple usando el vectorstore de FAQs como predeterminado
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectorstore_faqs.as_retriever(),
    return_source_documents=True,
)

# Hacer una pregunta
pregunta = "¿Qué es un agente RAG?"
respuesta = qa_chain.invoke({"query": pregunta})
print(respuesta['result'])

# Hacer una pregunta
pregunta = "¿Cuáles son los elementos de un agente RAG?"
respuesta = qa_chain.invoke({"query": pregunta})
print(respuesta['result'])

# Hacer una pregunta
pregunta = "¿Cual es la tarea de cada elemento un agente RAG?"
respuesta = qa_chain.invoke({"query": pregunta})
print(respuesta['result'])