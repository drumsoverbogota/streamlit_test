import os.path
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.llms.ollama import Ollama

import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))


# check if storage already exists
PERSIST_DIR = "./storage"
if not os.path.exists(PERSIST_DIR):

    documents = SimpleDirectoryReader("data").load_data()

    # nomic embedding model
    Settings.embed_model = OllamaEmbedding(model_name="nomic-embed-text")

    # ollama
    Settings.llm = Ollama(model="llama3", request_timeout=360.0)

    index = VectorStoreIndex.from_documents(
        documents,
    )
else:
    # load the existing index
    storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
    index = load_index_from_storage(storage_context)

# Either way we can now query the index
query_engine = index.as_query_engine()
response = query_engine.query("What did the author do growing up?")
print(response)