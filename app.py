# import streamlit as st
# from streamlit_option_menu import option_menu
# from streamlit_extras.switch_page_button import switch_page

# def navigation_bar():
#     selected = option_menu(
#         menu_title=None,
#         options=["Home", "Upload File", "Files", 'Chats', 'Contact'],
#         icons=['house', 'cloud-upload', "database", 'chat', 'phone'],
#         menu_icon="cast",
#         default_index=0,
#         orientation="horizontal",
#         styles={
#             "container": {"padding": "0!important", "background-color": "#3498DB"},
#             "icon": {"color": "white", "font-size": "25px"},
#             "nav-link": {"font-size": "18px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
#             "nav-link-selected": {"background-color": "#2C3E50"},
#         }
#     )
    
#     st.markdown('<style>div[data-testid="stHorizontalBlock"] {margin-top: -60px;}</style>', unsafe_allow_html=True)
#     return selected

# def main():
#     st.set_page_config(layout="wide")
#     selected = navigation_bar()
    
#     st.sidebar.title("This is the title of the sidebar")
#     st.sidebar.button("Tap here")
#     st.sidebar.radio("Pick your type", ['Male', 'Female'])

#     if selected == "Home":
#         st.title("Welcome to your doc reader app assistant!")
        
#         # Add space between the title and the sections
#         st.markdown("<div style='margin-top: 50px;'></div>", unsafe_allow_html=True)
        
#         # Center the sections
#         st.markdown("<div style='display: flex; justify-content: center;'>", unsafe_allow_html=True)
        
#         col1, col2, col3 = st.columns(3)

#         with col1:
#             st.markdown(f'<div class="section section1">', unsafe_allow_html=True)
#             st.header(":green-background[Upload File]")
#             st.write("Upload the file to be summarized.")
#             if st.button('Go to doc Upload'):
#                 switch_page("upload_file")
#                 # selected = 'Upload File'
#             st.markdown('</div>', unsafe_allow_html=True)

#         with col2:
#             st.markdown('<div class="section section2">', unsafe_allow_html=True)
#             st.header(":blue-background[Files]")
#             st.write("Access your uploaded files.")
#             if st.button('Go to Files'):
#                 switch_page("Files")
#                 # selected = 'Files'
#             st.markdown('</div>', unsafe_allow_html=True)

#         with col3:
#             st.markdown('<div class="section section3">', unsafe_allow_html=True)
#             st.header(":red-background[Chats]")
#             st.write("Access your chats with your docs.")
#             if st.button('Go to Chats'):
#                 switch_page("Chats")
#                 # selected = 'Chats'
#             st.markdown('</div>', unsafe_allow_html=True)

#         st.markdown("</div>", unsafe_allow_html=True)


#     # if selected == "Home":
#     #     switch_page("app")
#     elif selected == "Upload File":
#         switch_page("upload_file")
#     elif selected == "Files":
#         switch_page("files")
#     elif selected == "Chats":
#         switch_page("chats")
#     elif selected == "Contact":
#         switch_page("contact")

# if __name__ == "__main__":
#     main()

# -------
# import streamlit as st
# from streamlit_extras.switch_page_button import switch_page
# from navigation import navigation_bar

# def load_home_page():
#     st.title("Welcome to your doc reader app assistant!")
    
#     # Add space between the title and the sections
#     st.markdown("<div style='margin-top: 50px;'></div>", unsafe_allow_html=True)
    
#     # Center the sections
#     st.markdown("<div style='display: flex; justify-content: center;'>", unsafe_allow_html=True)
    
#     col1, col2, col3 = st.columns(3)

#     # Define the styles for each section
#     section_style = """
#     <style>
#     .section {
#         border: 2px solid;
#         border-radius: 10px;
#         padding: 20px;
#         text-align: center;
#         margin: 10px;
#     }
#     .section1 {
#         border-color: #1abc9c;
#         background-color: #d5f5e3;  /* Light green background */
#     }
#     .section2 {
#         border-color: #3498db;
#         background-color: #d6eaf8;  /* Light blue background */
#     }
#     .section3 {
#         border-color: #e74c3c;
#         background-color: #f5c6cb;  /* Light red background */
#     }
#     </style>
#     """
    

#     with col1:
#         st.markdown(f'<div class="section section1">', unsafe_allow_html=True)
#         st.header(":green-background[Upload File]")
#         st.write("Upload the file to be summarized.")
#         if st.button('Go to Upload File'):
#             switch_page("upload_file")
#         st.markdown('</div>', unsafe_allow_html=True)

#     with col2:
#         st.markdown('<div class="section section2">', unsafe_allow_html=True)
#         st.header(":blue-background[Files]")
#         st.write("Access your uploaded files.")
#         if st.button('Go to Files'):
#             switch_page("files")
#         st.markdown('</div>', unsafe_allow_html=True)

#     with col3:
#         st.markdown('<div class="section section3">', unsafe_allow_html=True)
#         st.header(":red-background[Chats]")
#         st.write("Access your chats with your docs.")
#         if st.button('Go to Chats'):
#             switch_page("chats")
#         st.markdown('</div>', unsafe_allow_html=True)

#     st.markdown("</div>", unsafe_allow_html=True)

# def main():
#     st.set_page_config(layout="wide")
#     selected = navigation_bar()
    
#     st.sidebar.title("This is the title of the sidebar")
#     st.sidebar.button("Tap here")
#     st.sidebar.radio("Pick your type", ['Male', 'Female'])

#     if selected == "Home":
#         load_home_page()
#     elif selected == "Upload File":
#         switch_page("upload_file")
#     elif selected == "Files":
#         switch_page("files")
#     elif selected == "Chats":
#         switch_page("chats")
#     elif selected == "Contact":
#         switch_page("contact")

# if __name__ == "__main__":
#     main()


## -------------
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_extras.switch_page_button import switch_page
# from advanced_chatbot.services.rag_service import RagService  # Import the RAG service

def navigation_bar():
    selected = option_menu(
        menu_title=None,
        options=["Home", "Upload File", "Files", "Chats", "Contact"],
        icons=['house', 'cloud-upload', "database", 'chat', 'phone'],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#3498DB"},
            "icon": {"color": "white", "font-size": "25px"},
            "nav-link": {"font-size": "18px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#2C3E50"},
        }
    )
    
    st.markdown('<style>div[data-testid="stHorizontalBlock"] {margin-top: -60px;}</style>', unsafe_allow_html=True)
    return selected

def main():
    st.set_page_config(layout="wide")
    selected = navigation_bar()
    
    st.sidebar.title("")# This is the title of the sidebar
    # st.sidebar.button("Tap here")
    # st.sidebar.radio("Pick your type", ['Male', 'Female'])

    if selected == "Home":
        st.title("Welcome to your doc reader app assistant!")
        
        # Add space between the title and the sections
        st.markdown("<div style='margin-top: 50px;'></div>", unsafe_allow_html=True)
        
        # Center the sections
        st.markdown("<div style='display: flex; justify-content: center;'>", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown(f'<div class="section section1">', unsafe_allow_html=True)
            st.header(":green-background[Upload File]")
            st.write("Upload the file to be summarized.")
            if st.button('Go to doc Upload'):
                switch_page("upload_file")
            st.markdown('</div>', unsafe_allow_html=True)

        with col2:
            st.markdown('<div class="section section2">', unsafe_allow_html=True)
            st.header(":blue-background[Files]")
            st.write("Access your uploaded files.")
            if st.button('Go to Files'):
                switch_page("Files")
            st.markdown('</div>', unsafe_allow_html=True)

        with col3:
            st.markdown('<div class="section section3">', unsafe_allow_html=True)
            st.header(":red-background[Chats]")
            st.write("Access your chats with your docs.")
            if st.button('Go to Chats'):
                switch_page("Chats")
            st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

    elif selected == "Upload File":
        switch_page("upload_file")
    elif selected == "Files":
        switch_page("files")
    elif selected == "Chats":
        switch_page("chats")
    elif selected == "Contact":
        switch_page("contact")

if __name__ == "__main__":
    main()
