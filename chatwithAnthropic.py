# Required packages
# !pip install streamlit anthropic python-dotenv

# Importing required packages
import os
import streamlit as st
import anthropic
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set the title of the Streamlit app
st.title("Chat with Claude 3 Opus")

# Initialize the Anthropic client with API key
client = anthropic.Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY"),
)

# Check if 'anthropic_model' is in session state, if not set it to 'claude-3-opus-20240229'
if "anthropic_model" not in st.session_state:
    st.session_state["anthropic_model"] = "claude-3-opus-20240229" # Use any model that Anthropic supports from https://docs.anthropic.com/claude/docs/models-overview

# Check if 'messages' is in session state, if not set it to an empty list
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display the messages in the chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Get the user's move and add it to the messages
if prompt := st.chat_input("Your move:"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate the assistant's response using Anthropic and add it to the messages
    with st.chat_message("assistant"):
        with client.messages.stream(
            model=st.session_state["anthropic_model"],
            max_tokens=1024,
            temperature=0,
            system="You are a helpful assistant.",
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],            
        ) as stream:
            full_response = ""
            for text in stream.text_stream:
                full_response += text
            st.markdown(full_response, unsafe_allow_html=True)
            st.session_state.messages.append({"role": "assistant", "content": full_response})
