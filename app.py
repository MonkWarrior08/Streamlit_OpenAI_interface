from openai import OpenAI
import streamlit as st
from PyPDF2 import PdfReader


# Add a sidebar for LangChain
st.sidebar.title("Dimi's OpenAI")
st.sidebar.write("By [Monkwarrior08](https://github.com/MonkWarrior08)")
# Add a text input for the API key in the sidebar
api_key = st.sidebar.text_input("Enter your OpenAI API Key", type="password")


# Add a dropdown for model selection
model_options = ["gpt-4o", "gpt-4o-mini", "o1-mini", "o1-preview"]
selected_model = st.sidebar.selectbox("OpenAI model", model_options)


# Initialize the OpenAI client with the user-provided API key
client = OpenAI(api_key=api_key)

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = selected_model

# Update the model if the user changes the selection
if st.session_state["openai_model"] != selected_model:
    st.session_state["openai_model"] = selected_model


if "messages" not in st.session_state:
    st.session_state.messages = []

# Add a text input for a custom system prompt in the sidebar
custom_system_prompt = st.sidebar.text_area("Custom System Prompt", "")

# Store the custom system prompt in session state
st.session_state["custom_system_prompt"] = custom_system_prompt


# Modify the file uploader to accept multiple files
uploaded_files = st.sidebar.file_uploader("Upload documents", type=["txt", "pdf"], accept_multiple_files=True)

# Process each uploaded file
file_contents = []
if uploaded_files:
    for uploaded_file in uploaded_files:
        file_content = ""

        if uploaded_file.type == "application/pdf":
            # Read PDF file
            pdf_reader = PdfReader(uploaded_file)
            for page in pdf_reader.pages:
                file_content += page.extract_text()
        else:
            # Read and decode text file
            try:
                file_content = uploaded_file.read().decode("utf-8")
            except UnicodeDecodeError:
                st.error(f"The uploaded file {uploaded_file.name} could not be decoded.")
                file_content = ""

        # Truncate the file content if it's too long
        max_length = 16000 
        if len(file_content) > max_length:
            file_content = file_content[:max_length]

        # Append the file content to the list
        file_contents.append(file_content)

    # Store all file contents in session state for AI use
    st.session_state["file_contents"] = file_contents


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What's on your mind Dimitri?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # Include the file contents and custom system prompt in the messages if available
        messages = [
            {"role": m["role"], "content": m["content"]}
            for m in st.session_state.messages
        ]
        if "file_contents" in st.session_state and st.session_state["file_contents"]:
            for content in st.session_state["file_contents"]:
                messages.append({"role": "system", "content": content})
        
        # Add the custom system prompt to the messages
        if st.session_state["custom_system_prompt"]:
            messages.append({"role": "system", "content": st.session_state["custom_system_prompt"]})

        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=messages,
            stream=True
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})


# Add a button to clear messages in the sidebar
if st.sidebar.button("Clear Chat"):
    st.session_state.messages = []
    st.session_state["file_contents"] = []  # Clear file contents
    st.session_state["custom_system_prompt"] = ""  # Clear custom system prompt