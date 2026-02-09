from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama


Settings.llm = Ollama(
    model="llama3",
    request_timeout=120.0
)

Settings.embed_model = HuggingFaceEmbedding(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

docs = SimpleDirectoryReader("data/regulatory_docs").load_data()

index = VectorStoreIndex.from_documents(docs)

index.storage_context.persist("storage")

print("✅ Index created!")
