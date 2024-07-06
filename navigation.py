# import streamlit as st
# from streamlit_option_menu import option_menu

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
#---------

import streamlit as st
from streamlit_option_menu import option_menu

def navigation_bar():
    selected = option_menu(
        menu_title=None,
        options=["Home", "Upload File", "Files", 'Chats', 'Contact'],
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
