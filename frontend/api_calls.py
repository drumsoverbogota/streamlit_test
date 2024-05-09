from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    load_index_from_storage,
)

import logging
import sys
import os

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))





class ChatBot:

    def __init__(self) -> None:
        PERSIST_DIR = "storage/"
        if not os.path.exists(PERSIST_DIR):
            # load the documents and create the index
            documents = SimpleDirectoryReader("data").load_data()
            print("loading data")
            index = VectorStoreIndex.from_documents(documents)
            # store it for later
            index.storage_context.persist(persist_dir=PERSIST_DIR)
        else:
            # load the existing index
            storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
            index = load_index_from_storage(storage_context)
        query_engine = self.index.as_query_engine()
        response = query_engine.query("What did the author do growing up?")
        print(response)

    def generate_response(self, user, prompt_input):
        query_engine = self.index.as_query_engine()
        response = query_engine.query("What did the author do growing up?")
        return response


    def _retrieve_history(self, user):
        pass