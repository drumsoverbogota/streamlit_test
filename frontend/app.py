import streamlit as st
from streamlit_msal import Msal
import requests
import os

from api_calls import ChatBot
import logging

from opencensus.ext.azure.log_exporter import AzureLogHandler

#client_id = "1a9575e1-2beb-4b58-8fcf-5f61b6233672"
#authority = "https://login.microsoftonline.com/badb3c2c-4a15-425a-8561-883f47405264"

client_id = os.environ.get("msal_client_id")
authority = os.environ.get("msal_authority")
instrumentation_key = os.environ.get("instrumentation_key")

# App title
st.set_page_config(page_title="A Chatbot!")

def api_call(prompt: str):
    data_body = {"prompt": prompt}
    response = requests.post("http://127.0.0.1:8000/chat", json=data_body).json()
    return response.get("response")

# Initializations

if "logged_in" not in st.session_state.keys():
    st.session_state.logged_in = False

if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "Please Login"}]

if "logger_module" not in st.session_state.keys():
    logger = logging.getLogger(__name__)

    if instrumentation_key:
        logger.addHandler(AzureLogHandler(connection_string=f'InstrumentationKey={instrumentation_key}'))

    st.session_state.logger_module = logger



for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

with st.sidebar:
    st.title('Small chatbot test')
    if client_id and authority:
        auth_data = Msal.initialize_ui(
            client_id=client_id,
            authority=authority,
            scopes=[], # Optional
            # Customize (Default values):
            connecting_label="Connecting",
            disconnected_label="Disconnected",
            sign_in_label="Sign in",
            sign_out_label="Sign out"
        )
    else:
        auth_data = None

if not auth_data and not (client_id or authority):
    st.write("Authenticate to access protected content")
    st.stop()
elif not st.session_state.logged_in:
    st.session_state.logged_in = True
    user_name = auth_data.get("account", {"name": "No Name"})["name"]
    st.session_state.messages = [{"role": "assistant", "content": f"Hi! {user_name}, Welcome back!"}]

if prompt := st.chat_input(disabled=not auth_data):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

# Generate a new response if last message is not from assistant
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            #response = chat.generate_response("me", prompt)
            response = f"hola: {prompt}" 
            st.session_state.logger_module.info(f"the response was: {response}")
            placeholder = st.empty()
            full_response = ''
            for item in response:
                full_response += item
                placeholder.markdown(full_response)
            placeholder.markdown(full_response)
    message = {"role": "assistant", "content": full_response}
    st.session_state.messages.append(message)
