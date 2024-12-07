from openai import OpenAI
import streamlit as st
from PyPDF2 import PdfReader



# Add a sidebar for LangChain
st.sidebar.title("OpenAI Chat")


# Add a dropdown for model selection
model_options = ["gpt-4o", "gpt-4o-mini", "o1-mini", "o1-preview"]
selected_model = st.sidebar.selectbox("OpenAI model", model_options)

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

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


# Add a file uploader in the sidebar
uploaded_file = st.sidebar.file_uploader("Upload a document", type=["txt", "pdf"])

# Process the uploaded file
if uploaded_file is not None:
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
            st.error("The uploaded file could not be decoded.")
            file_content = ""

    # Truncate the file content if it's too long
    max_length = 16000 
    if len(file_content) > max_length:
        file_content = file_content[:max_length]

    # Store the file content in session state for AI use
    st.session_state["file_content"] = file_content


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Anything in mind?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # Include the file content and custom system prompt in the messages if available
        messages = [
            {"role": m["role"], "content": m["content"]}
            for m in st.session_state.messages
        ]
        if "file_content" in st.session_state and st.session_state["file_content"]:
            messages.append({"role": "system", "content": st.session_state["file_content"]})
        
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