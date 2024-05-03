import streamlit as st
import requests

replicate_api = "Aaaaa"
#replicate_api = None

# App title
st.set_page_config(page_title="A Chatbot!")

def api_call(prompt: str):
    data_body = {"prompt": prompt}
    print(data_body)
    response = requests.post("http://127.0.0.1:8000/chat", json=data_body).json()
    print(response)
    return response.get("response")

if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

with st.sidebar:
    st.title('Small chatbot test')


if prompt := st.chat_input(disabled=not replicate_api):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

# Generate a new response if last message is not from assistant
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = api_call(prompt)
            placeholder = st.empty()
            full_response = ''
            for item in response:
                full_response += item
                placeholder.markdown(full_response)
            placeholder.markdown(full_response)
    message = {"role": "assistant", "content": full_response}
    st.session_state.messages.append(message)