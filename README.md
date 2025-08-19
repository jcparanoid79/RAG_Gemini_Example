# Proyecto Agente RAG con Gemini

Este proyecto implementa un agente de Generación Aumentada por Reclutamiento (RAG) utilizando los modelos de Google Gemini. El agente puede responder preguntas basadas en un conjunto de documentos proporcionados.

## Descripción

El sistema utiliza una base de datos vectorial (FAISS) para almacenar los embeddings de los documentos y encontrar los más relevantes para una pregunta dada. Luego, utiliza un modelo de lenguaje de Gemini para generar una respuesta basada en esos documentos.

## Características

-   Ingesta de documentos de texto (`.txt`).
-   Creación de un índice vectorial con FAISS.
-   Consultas en lenguaje natural.
-   Generación de respuestas con contexto utilizando Gemini.

## Requisitos

-   Python 3.8 o superior
-   Bibliotecas de Python (ver `requirements.txt`)
-   Una clave de API de Google

## Instalación

1.  Clona este repositorio:
    ```bash
    git clone https://github.com/tu-usuario/tu-repositorio.git
    cd tu-repositorio
    ```

2.  Crea un entorno virtual e instálalo:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # En Windows usa `.venv\Scripts\activate`
    ```

3.  Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

4.  Configura tu clave de API de Google en un archivo `.env`:
    ```
    GOOGLE_API_KEY="TU_API_KEY"
    ```

## Uso

### 1. Ingesta de Datos

Para procesar tus documentos y crear el índice vectorial, ejecuta el script `ingestor.py`:

```bash
python src/ingestor.py
```

### 2. Realizar Consultas

Para iniciar el agente y hacerle preguntas, ejecuta el script `agente_rag.py`:

```bash
python src/agente_rag.py
```

Escribe tu pregunta en la consola y presiona Enter. Para salir, escribe 'salir'.

## Estructura del Proyecto

```
.
├── .github/              # Workflows de GitHub (CI/CD)
├── .venv/                # Entorno virtual de Python
├── data/                 # Archivos de datos (txt, csv, etc.)
│   ├── comunicados.txt
│   ├── docs_tecnicos.txt
│   └── faqs.txt
├── docs/                 # Documentación del proyecto
├── faiss_index_.../      # Índices de FAISS generados
├── src/                  # Código fuente
│   ├── __init__.py
│   ├── agente_rag.py
│   └── ingestor.py
├── tests/                # Pruebas unitarias y de integración
│   ├── __init__.py
│   └── test_agente.py
├── .env                  # Archivo de variables de entorno
├── .gitignore            # Archivos y directorios a ignorar por Git
├── LICENSE               # Licencia del proyecto
├── README.md             # Este archivo
└── requirements.txt      # Dependencias de Python
```

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.