# import streamlit as st

# def main():
#     st.title("Contact")
#     st.write("This is the contact page.")

# if __name__ == "__main__":
#     main()

#----------
# import streamlit as st
# from navigation import navigation_bar
# from streamlit_extras.switch_page_button import switch_page

# def main():
#     st.set_page_config(layout="wide")
#     selected = navigation_bar()

#     if selected != "Contact":
#         switch_page(selected)

#     st.title("Contact")
#     st.write("This is the contact page.")

# if __name__ == "__main__":
#     main()
#-------- 

import streamlit as st
from navigation import navigation_bar
from streamlit_extras.switch_page_button import switch_page

def main():
    st.set_page_config(layout="wide")
    selected = navigation_bar()

    # if selected != "Contact":
    #     switch_page(selected)

    st.title("Contact")
    st.write("This is the contact page.")

    st.write("For support, contact us at:")
    st.write("Email: support@example.com")
    st.write("Phone: +1234567890")

if __name__ == "__main__":
    main()
