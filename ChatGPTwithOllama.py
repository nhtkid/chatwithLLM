import requests
import streamlit as st
import json

st.title("ChatGPT with Local LLM with Ollama")

# URL of the local Ollama server
OLLAMA_API_URL = "http://localhost:11434/api/chat" # This is the default port

# Model to use
OLLAMA_MODEL = "phi3"  # Replace with your desired model, check Ollama website for supported models

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle user input
if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Prepare payload for Ollama API
    payload = {
        "model": OLLAMA_MODEL,
        "messages": [
            {"role": m["role"], "content": m["content"]}
            for m in st.session_state.messages
        ],
    }

    # Make a request to Ollama API
    response = requests.post(OLLAMA_API_URL, json=payload, stream=True)

    assistant_reply = ""
    for chunk in response.iter_lines():
        if chunk:
            chunk_data = chunk.decode('utf-8')
            json_chunk = None
            try:
                json_chunk = json.loads(chunk_data)
            except json.JSONDecodeError:
                continue

            if json_chunk and "message" in json_chunk and "content" in json_chunk["message"]:
                assistant_reply += json_chunk["message"]["content"]

    with st.chat_message("assistant"):
        st.markdown(assistant_reply)

    st.session_state.messages.append({"role": "assistant", "content": assistant_reply})
