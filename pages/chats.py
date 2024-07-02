# import streamlit as st

# def main():
#     st.title("Chats")
#     st.write("This is the page to access your chats with your docs.")

# if __name__ == "__main__":
#     main()

#------------
# import streamlit as st
# from navigation import navigation_bar
# from streamlit_extras.switch_page_button import switch_page

# def main():
#     st.set_page_config(layout="wide")
#     selected = navigation_bar()

#     if selected != "Chats":
#         switch_page(selected)

#     st.title("Chats")
#     st.write("This is the page to access your chats with your docs.")

# if __name__ == "__main__":
#     main()
#------------

# # Version 0
# import streamlit as st
# from navigation import navigation_bar
# from streamlit_extras.switch_page_button import switch_page
# from advanced_chatbot.services.rag_service import RagService  # Import the RAG service

# def main():
#     st.set_page_config(layout="wide")
#     selected = navigation_bar()

#     if selected != "Chats":
#         switch_page(selected)

#     st.title("Chats")
#     st.write("This is the page to access your chats with your docs.")

#     index_ids = [config['index_id'] for config in RagService.list_vector_store_index()]
#     selected_index_ids = st.multiselect("Select documents for the chat", index_ids)

#     if selected_index_ids:
#         conversation_history = []
#         user_input = st.text_input("Ask your question")
#         if st.button("Submit"):
#             response_generator, source_nodes = RagService.complete_chat(
#                 query=user_input,
#                 conversation_history=conversation_history,
#                 index_ids=selected_index_ids
#             )
#             response = "".join([chunk for chunk in response_generator])
#             st.write(response)
#             conversation_history.append({"role": "user", "content": user_input})
#             conversation_history.append({"role": "assistant", "content": response})

# if __name__ == "__main__":
#     main()

#__________
# import streamlit as st
# from navigation import navigation_bar
# from streamlit_extras.switch_page_button import switch_page
# from advanced_chatbot.services.rag_service import RagService  # Import the RAG service

# def main():
#     st.set_page_config(layout="wide")
#     selected = navigation_bar()

#     # if selected != "Chats":
#     #     switch_page(selected)

#     st.title("Chats")
#     st.write("This is the page to access your chats with your docs.")

#     index_ids = [config['index_id'] for config in RagService.list_vector_store_index()]
#     selected_index_ids = st.multiselect("Select documents for the chat", index_ids)

#     if selected_index_ids:
#         conversation_history = []
#         user_input = st.text_input("Ask your question")
#         if st.button("Submit"):
#             response, source_nodes = RagService.complete_chat(
#                 query=user_input,
#                 conversation_history=conversation_history,
#                 index_ids=selected_index_ids
#             )
#             st.write(response)
#             conversation_history.append({"role": "user", "content": user_input})
#             conversation_history.append({"role": "assistant", "content": response})

# if __name__ == "__main__":
#     main()

#--------
import streamlit as st
from navigation import navigation_bar
from streamlit_extras.switch_page_button import switch_page
from advanced_chatbot.services.rag_service import RagService  # Import the RAG service

def main():
    st.set_page_config(layout="wide")
    selected = navigation_bar()

    # if selected != "Chats":
    #     switch_page(selected)

    with st.sidebar:
        st.title("Chats")

    st.write("This is the page to access your chats with your docs.")

    index_ids = [config['index_id'] for config in RagService.list_vector_store_index()]

    with st.form(key='chat_form'):
        selected_index_ids = st.multiselect("Select documents for the chat", index_ids)
        conversation_history = st.session_state.get('conversation_history', [])

        user_input = st.text_input("Ask your question")

        if st.form_submit_button("Submit"):
            response, source_nodes = RagService.complete_chat(
                query=user_input,
                conversation_history=conversation_history,
                index_ids=selected_index_ids
            )
            st.write(response)
            conversation_history.append({"role": "user", "content": user_input})
            conversation_history.append({"role": "assistant", "content": response})

        # Save conversation history in session state
        st.session_state['conversation_history'] = conversation_history

if __name__ == "__main__":
    main()
