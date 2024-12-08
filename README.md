# OpenAI-Chat-interface
### Link: https://openaichatinterface.streamlit.app/

<img width="1787" alt="Screenshot 2024-12-08 at 6 30 28 PM" src="https://github.com/user-attachments/assets/22e16bac-607d-49e3-a060-34587a106a9c">

A Streamlit-based web application that provides an interactive chat interface powered by OpenAI's language models. This application allows users to have conversations with AI models while also incorporating document analysis capabilities.

## ✨ Features

- 🤖 Interactive chat interface with OpenAI models
- 📁 Support for multiple document uploads (PDF and TXT files)
- 🔄 Model selection flexibility
- 💬 Custom system prompt configuration
- 🧹 Chat history management
- 📝 Real-time streaming responses

## 🚀 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/MonkWarrior08/OpenAI_Chat_interface.git
cd OpenAI_Chat_interface
```

### 2. Set Up Virtual Environment

#### Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

#### Requirements
```txt
openai>=1.0.0
streamlit>=1.24.0
PyPDF2>=3.0.0
```


## 💻 Usage

### Starting the Application
```bash
streamlit run app.py
```

### Access the Interface
Open your browser and navigate to:
- Local URL: `http://localhost:8501`

### Available Features
- 🔑 API Key Input: Enter your OpenAI API Key
- 🔄 Model Selection: Choose from different OpenAI models
- 📁 Document Upload: Support for PDF and TXT files
- ⚙️ System Prompts: Customize AI behavior
- 💬 Chat Interface: Real-time conversation
- 🧹 Clear Chat: Reset conversation history

## 🎯 Interface Components

### Sidebar Controls
- 📊 Model selection dropdown
- 📎 Document upload functionality
- ⌨️ Custom system prompt input
- 🔄 Clear chat button

### Main Chat Area
- 💬 Real-time chat interaction
- 📜 Message history display
- ⚡ Streaming response output

## 🤝 Contributing
Contributions are welcome! For major changes:
1. Fork the repository
2. Create your feature branch
3. Open a pull request

## 📄 License
[MIT](https://choosealicense.com/licenses/mit/)

## 👨‍💻 Author
Created with ❤️ by [Monkwarrior08](https://github.com/MonkWarrior08)
