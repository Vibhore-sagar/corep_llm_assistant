from llama_index.core import load_index_from_storage, StorageContext, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama


# ✅ Tell LlamaIndex to use LOCAL LLM
Settings.llm = Ollama(
    model="llama3",
    request_timeout=120.0
)

# ✅ Local embeddings
Settings.embed_model = HuggingFaceEmbedding(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

storage_context = StorageContext.from_defaults(
    persist_dir="storage"
)

index = load_index_from_storage(storage_context)

query_engine = index.as_query_engine(
    similarity_top_k=3
)


def retrieve_context(query: str):
    response = query_engine.query(query)
    return str(response)
