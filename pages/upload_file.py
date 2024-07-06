#--------
import streamlit as st
from navigation import navigation_bar
from app import main as app_main
from streamlit_option_menu import option_menu
from streamlit_extras.switch_page_button import switch_page
import fitz  # PyMuPDF
from docx import Document
import base64, os
import streamlit.components.v1 as components
from pathlib import Path
from advanced_chatbot.services.rag_service import RagService  # Import the RAG service

def save_uploaded_file(uploaded_file):
    # Specify the directory path
    directory = Path("uploaded_files")
    # Create the directory if it doesn't exist
    directory.mkdir(parents=True, exist_ok=True)
    save_path = Path("uploaded_files") / uploaded_file.name
    if uploaded_file.name not in os.listdir('uploaded_files'):
        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        return save_path
    else:
        st.write('⚠️ This file already exist in your uploaded files!')
        return None

def display_pdf(file):
    
    base64_pdf = base64.b64encode(file.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

def display_docx(file):
    doc = Document(file)
    for para in doc.paragraphs:
        st.write(para.text)


def main():
    st.set_page_config(layout="wide")
    navigation_bar()
    
    st.title("Upload File & Preview")
    st.write("This is the page to upload your files.")
    uploaded_files = st.file_uploader("Upload your document (⚠️ docx or pdf file only)", accept_multiple_files=True, type=['pdf', 'docx'])
    
    for uploaded_file in uploaded_files:
        st.write(f"Filename: {uploaded_file.name}")
        file_path = save_uploaded_file(uploaded_file)
        if file_path != None:
            RagService.create_vector_store_index(file_path)  # Create index for the uploaded file
            if uploaded_file.type == "application/pdf":
                # st.title("PDF Preview in Streamlit")
                display_pdf(uploaded_file)
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            display_docx(uploaded_file)

if __name__ == "__main__":
    main()
