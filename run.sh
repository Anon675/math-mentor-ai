#!/usr/bin/env bash

set -e

echo "Starting Math Mentor AI..."

echo "Checking Python environment..."
python --version

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Building vector store if not present..."

if [ ! -f "vector_store/index.faiss" ]; then
  echo "Initializing RAG vector database..."

  python <<EOF
from rag.knowledge_loader import KnowledgeLoader
from rag.chunker import TextChunker
from rag.embeddings import EmbeddingModel
from rag.vector_store import VectorStore

loader = KnowledgeLoader()
docs = loader.load_documents()

chunker = TextChunker()
chunks = chunker.chunk(docs)

embedder = EmbeddingModel()
embeddings = embedder.encode(chunks)

store = VectorStore()
store.build(embeddings, chunks)

print("Vector store created successfully")
EOF

else
  echo "Vector store already exists."
fi

echo "Launching Streamlit application..."

streamlit run app.py