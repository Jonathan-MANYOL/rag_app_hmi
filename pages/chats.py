import streamlit as st
from navigation import navigation_bar
from streamlit_extras.switch_page_button import switch_page
from advanced_chatbot.services.rag_service import RagService  # Import the RAG service

def main():
    st.set_page_config(layout="wide")
    selected = navigation_bar()
    st.title(":blue-background[Chats]")
    # if selected != "Chats":
    #     switch_page(selected)

    with st.sidebar:
        st.title("Chats")

    st.write("This is the page to access your chats with your docs.")

    index_ids = [config['index_id'] for config in RagService.list_vector_store_index()]

    # with st.form(key='chat_form'):
    selected_index_ids = st.multiselect("Select documents for the chat", index_ids)
    conversation_history = st.session_state.get('conversation_history', [])

    # Improved chat
    chat_zone = st.container()
    messages = st.container(height=300)

    try:
        # Initialize chat history
        if "messages" not in st.session_state:
            st.session_state.messages = []

        # Translate and summurize first page
        # if selected_index_ids:
        #     for id in selected_index_ids:
        #         st.write(id)
        #         with messages.chat_message('assistant'):
        #             res = RagService.translate_and_summarize_first_page_fr(id)
        #             st.write_stream(res)
        #         st.session_state.messages.append({"role": "assistant", "content": res})

        if prompt := st.chat_input("Say something"): # Accept user input
            # # Initialize chat history
            # if "messages" not in st.session_state:
            #     st.session_state.messages = []

            # # Translate and summurize first page
            # if selected_index_ids:
            #     for id in selected_index_ids:
            #         with messages.chat_message('assistant'):
            #             res = RagService.translate_and_summarize_first_page_fr(id)
            #             st.write_stream(res)
            #         st.session_state.messages.append({"role": "assistant", "content": res})
            
            # Display chat messages from history on app rerun
            for message in st.session_state.messages:
                with messages.chat_message(message["role"]):
                    st.markdown(message["content"])
            
            # Display user message in chat message container
            with messages.chat_message("user"):
                st.markdown(prompt)
                # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": prompt})

            if selected_index_ids:
                # Display assistant response in chat message container
                with messages.chat_message("assistant"):
                    
                    response, source_nodes = RagService.complete_chat(
                            query=prompt,
                            conversation_history= st.session_state.messages,#conversation_history,
                            index_ids=selected_index_ids )
                    response = st.write_stream(response)
                    # Add assistant response to chat history
                    for node in source_nodes:
                        st.write(f"Source node content: {node.get_text()}")
                st.session_state.messages.append({"role": "assistant", "content": response})
            else:
                raise(ZeroDivisionError)
            
            
    
    except ZeroDivisionError: 
        with messages.chat_message("assistant"):
            response = '⚠️ You must at least select a document to chat with!'
            st.write(response)
        # Add user message to chat history
        # st.session_state.messages.append({"role": "user", "content": prompt})
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})



if __name__ == "__main__":
    main()
