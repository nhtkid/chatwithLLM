# Install necessary packages
# pip install streamlit groq dotenv

import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up Streamlit app with any title you like
st.title("Chess with LLaMA3 70b")

# Initialize Groq client with API key from environment variable
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# Manage session state using Streamlit's st.session_state
if "groq_model" not in st.session_state:
    st.session_state["groq_model"] = "llama3-70b-8192" # Use the modelid from https://console.groq.com/docs/models

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display existing chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Prompt user for input, you can type any placeholder text
if prompt := st.chat_input("What is up?"):
    # Add user input to messages list
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate response using Groq model
    with st.chat_message("assistant"):
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            model=st.session_state["groq_model"],
        )
        response = chat_completion.choices[0].message.content
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
