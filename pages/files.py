# import streamlit as st

# def main():
#     st.title("Files")
#     st.write("This is the page to access your uploaded files.")

# if __name__ == "__main__":
#     main()

#----------
# import streamlit as st
# from navigation import navigation_bar
# from streamlit_extras.switch_page_button import switch_page

# def main():
#     st.set_page_config(layout="wide")
#     selected = navigation_bar()

#     if selected != "Files":
#         switch_page(selected)

#     st.title("Files")
#     st.write("This is the page to access your uploaded files.")

# if __name__ == "__main__":
#     main()
#-----------

import streamlit as st
from navigation import navigation_bar
from streamlit_extras.switch_page_button import switch_page
from advanced_chatbot.services.rag_service import RagService  # Import the RAG service

def main():
    st.set_page_config(layout="wide")
    selected = navigation_bar()

    # if selected != "Files":
    #     switch_page(selected)

    st.title("Files")
    st.write("This is the page to access your uploaded files.")

    index_configs = RagService.list_vector_store_index()
    for config in index_configs:
        st.write(f"Index ID: {config['index_id']}")
        st.write(f"Document Path: {config['document_path']}")

        if st.button(f"Delete {config['index_id']}"):
            RagService.delete_vector_store_index(config['index_id'])
            st.experimental_rerun()

if __name__ == "__main__":
    main()
