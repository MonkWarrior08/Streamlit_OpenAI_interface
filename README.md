# OpenAI-Chat-interface

A Streamlit-based web application that provides an interactive chat interface powered by OpenAI's language models. This application allows users to have conversations with AI models while also incorporating document analysis capabilities.

## Features

- 🤖 Interactive chat interface with OpenAI models
- 📁 Support for multiple document uploads (PDF and TXT files)
- 🔄 Model selection flexibility
- 💬 Custom system prompt configuration
- 🧹 Chat history management
- 📝 Real-time streaming responses

## Installation

1. Clone the repository:
```bash
git clone https://github.com/MonkWarrior08/OpenAI_Chat_interface.git
cd OpenAI_Chat_interface
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your OpenAI API key in Streamlit's secrets:
Go to and open .streamlit/secrets.toml` file and insert your API key:
```toml
OPENAI_API_KEY = "your-api-key-here"
```

## Usage

1. Run the Streamlit application:
```bash
streamlit run app.py
```

2. Access the application through your web browser (typically at `http://localhost:8501`)

3. Features available in the interface:
   - Select different OpenAI models from the dropdown
   - Upload PDF or TXT files for analysis
   - Enter custom system prompts
   - Chat with the AI
   - Clear chat history when needed

## Interface Components

### Sidebar
- Model selection dropdown
- Document upload functionality
- Custom system prompt input
- Clear chat button

### Main Chat Interface
- Real-time chat interaction
- Message history display
- Streaming response output

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
