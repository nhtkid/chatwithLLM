# A Streamlit chatbot with OpenAI GPT models
# Required packages
# Install required packages
# pip install streamlit openai python-dotenv

# Importing required packages
import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set the title of the Streamlit app
st.title("Chat with GPT-4 Turbo")

# Initialize the OpenAI client with API key
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

# Check if 'openai_model' is in session state, if not set it to 'gpt-4-turbo'
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4-turbo" # Use any model that OpenAI supports from https://platform.openai.com/docs/models

# Check if 'messages' is in session state, if not set it to a default message
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "You are a helpful assistant"}]

# Display the messages in the chat
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Add any text to the user input placeholder
if prompt := st.chat_input("Your move:"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate the assistant's response using OpenAI and add it to the messages
    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            temperature=0,
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})
