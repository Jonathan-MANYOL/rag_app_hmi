# # import streamlit as st

# # def main():
# #     st.title("Upload File")
# #     st.write("This is the page to upload your files.")

# # if __name__ == "__main__":
# #     main()

# import streamlit as st
# from navigation import navigation_bar
# from streamlit_extras.switch_page_button import switch_page

# def main():
#     st.set_page_config(layout="wide", page_title='Upload file')
#     selected = navigation_bar()

    # if selected != "Upload File":
    #     if selected == 'home':
    #         switch_page('app')
    #     else:
    #         switch_page(selected)

#     st.title("Upload File")
#     st.write("This is the page to upload your files.")

# if __name__ == "__main__":
#     main()

# import streamlit as st
# from navigation import navigation_bar
# from app import main as app_main
# from streamlit_extras.switch_page_button import switch_page

# def main():
#     st.set_page_config(layout="wide")
#     #selected = navigation_bar()
#     #print(selected)

#     # if selected != "Upload File":
#     #     if selected == 'Home':
#     #         switch_page('app')
#     #     else:
#     #         switch_page(selected)

#     st.title(":green-background[pload File]")
#     st.write("This is the page to upload your files.")
#     uploaded_files = st.file_uploader("'Upload your document (⚠️ docx or pdf file only)'", accept_multiple_files=True, type=['pdf', 'docx'])
#     for uploaded_file in uploaded_files:
#         #bytes_data = uploaded_file.read()
#         st.write("filename:", uploaded_file.name)
#         st.write(uploaded_file.getvalue())#bytes_data)
# if __name__ == "__main__":
#     main()

#---------
# import streamlit as st
# from navigation import navigation_bar
# from app import main as app_main
# from streamlit_extras.switch_page_button import switch_page
# import fitz  # PyMuPDF
# from docx import Document
# import base64
# import streamlit.components.v1 as components

# def display_pdf(file):
    
#     st.title("PDF Preview in Streamlit")

#     if file is not None:
#         # Read the file
#         base64_pdf = base64.b64encode(file.read()).decode('utf-8')

#         # Embed PDF in HTML
#         pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'

#         st.markdown(pdf_display, unsafe_allow_html=True)

# def display_docx(file):
#     doc = Document(file)
#     for para in doc.paragraphs:
#         st.write(para.text)

# def main():
#     st.set_page_config(layout="wide")

#     st.title("Upload File")
#     st.write("This is the page to upload your files.")
#     uploaded_files = st.file_uploader("Upload your document (⚠️ docx or pdf file only)", accept_multiple_files=True, type=['pdf', 'docx'])
    
#     for uploaded_file in uploaded_files:
#         st.write(f"Filename: {uploaded_file.name}")
#         if uploaded_file.type == "application/pdf":
#             display_pdf(uploaded_file)
#         elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
#             display_docx(uploaded_file)

# if __name__ == "__main__":
#     main()

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
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return save_path

def display_pdf(file):
    st.title("PDF Preview in Streamlit")
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
    
    st.title("Upload File")
    st.write("This is the page to upload your files.")
    uploaded_files = st.file_uploader("Upload your document (⚠️ docx or pdf file only)", accept_multiple_files=True, type=['pdf', 'docx'])
    
    for uploaded_file in uploaded_files:
        st.write(f"Filename: {uploaded_file.name}")
        file_path = save_uploaded_file(uploaded_file)
        RagService.create_vector_store_index(file_path)  # Create index for the uploaded file
        if uploaded_file.type == "application/pdf":
            display_pdf(uploaded_file)
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            display_docx(uploaded_file)

if __name__ == "__main__":
    main()
