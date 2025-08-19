from dotenv import load_dotenv
import os
import sys
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS

# Agrega el directorio raíz del proyecto al sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Load environment variables from .env file
load_dotenv()

# Check for the API key
if "GOOGLE_API_KEY" not in os.environ:
    raise ValueError("GOOGLE_API_KEY not found in .env file.")

# Función para crear un índice vectorial para un archivo específico
def crear_indice(ruta_archivo, nombre_indice):
    with open(ruta_archivo, "r", encoding="utf-8") as f:
        texto = f.read()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = text_splitter.split_text(texto)

    # Reemplazar OpenAIEmbeddings por GoogleGenerativeAIEmbeddings
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    docsearch = FAISS.from_texts(chunks, embeddings)
    docsearch.save_local(f"faiss_index_{nombre_indice}")
    print(f"Índice '{nombre_indice}' creado y guardado.")

# Crear los índices para cada fuente
crear_indice("data/docs_tecnicos.txt", "tecnicos")
crear_indice("data/faqs.txt", "faqs")
crear_indice("data/comunicados.txt", "comunicados")