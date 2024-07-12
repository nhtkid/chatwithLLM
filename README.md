# 🤖 ChatwithLLM

ChatwithLLM is a collection of Streamlit-based chat interfaces for various Large Language Models (LLMs). This repository demonstrates how to create simple, interactive chat applications using different AI providers and models.

## 📁 Repository Contents

1. `chat_with_ollama.py`: Chat interface for local LLMs using Ollama.
2. `chat_with_claude.py`: Chat interface for Anthropic's Claude 3 Opus model.
3. `chat_with_gpt.py`: Chat interface for OpenAI's GPT models.
4. `chat_with_groq.py`: Chat interface for Groq's LLM models.

## 🌟 Features

- 💬 Interactive chat interfaces for multiple AI models
- 🖥️ Local LLM support with Ollama
- ☁️ Cloud-based LLM support with Anthropic, OpenAI, and Groq
- 🔄 Conversation history management
- 🌊 Streaming responses for a more dynamic chat experience

## 🛠️ Installation

1. Clone the repository:
   ```
   git clone https://github.com/nhtkid/chatwithLLM.git
   cd chatwithLLM
   ```

2. Install the required dependencies for all scripts:
   ```
   pip install streamlit anthropic python-dotenv openai groq
   ```

3. For the Ollama script, make sure you have Ollama installed and running locally.

## ⚙️ Configuration

1. Create a `.env` file in the root directory of the project.
2. Add your API keys to the `.env` file:
   ```
   ANTHROPIC_API_KEY=your_anthropic_api_key_here
   OPENAI_API_KEY=your_openai_api_key_here
   GROQ_API_KEY=your_groq_api_key_here
   ```

## 🚀 Usage

To run any of the chat interfaces, use the Streamlit CLI:

1. For Ollama chat:
   ```
   streamlit run chat_with_ollama.py
   ```

2. For Claude chat:
   ```
   streamlit run chat_with_claude.py
   ```

3. For GPT chat:
   ```
   streamlit run chat_with_gpt.py
   ```

4. For Groq chat:
   ```
   streamlit run chat_with_groq.py
   ```

Each script will launch a Streamlit app in your default web browser, where you can interact with the chosen LLM.

## 📝 Script Details

### chat_with_ollama.py
- Uses a local Ollama server to run LLMs
- Default model: phi3 (can be changed in the script)
- Streams responses for a more dynamic chat experience

### chat_with_claude.py
- Interfaces with Anthropic's Claude 3 Opus model
- Uses the latest Claude model available
- Streams responses for real-time interaction

### chat_with_gpt.py
- Connects to OpenAI's GPT models
- Default model: gpt-4-turbo (can be changed in the script)
- Includes a system message to set the assistant's behavior

### chat_with_groq.py
- Utilizes Groq's inference engine for various LLMs
- Default model: llama3-70b-8192 (can be changed in the script)
- Provides fast inference for supported models

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
