import json
import streamlit as st
import urllib.request
import urllib.parse

# Show title and description.

with st.container():

    col1, col2 = st.columns([2, 1], gap='medium')
    with col1:
        st.title("💬 Eleodora")
        st.write(
            "This is Eleodora. Lumina's AI Assistant. "
            "She's designed to be whomever you want, and act just like you. "
            "You can talk to her here:"
        )
        query = st.text_input("Enter your question", type="default")
        if not query:
            st.info("Please enter a question to continue.", icon="🗝️")
        else:
            url = "http://35.224.236.67:8000/ai"
            data = {"query": query}  

            try:
                encoded_data = json.dumps(data).encode("utf-8")

                request = urllib.request.Request(url, data=encoded_data, headers={"Content-Type": "application/json"})

                with urllib.request.urlopen(request) as response:
                    response_bytes = response.read()
                    response_str = response_bytes.decode("utf-8")  

                    try:
                        data = json.loads(response_str)
                        answer = data.get("answer", "I'm still learning, but I couldn't find an answer.")
                        st.write(answer)
                    except st.json.JSONDecodeError:
                        st.error(f"Error parsing response: {response_str}")

            except urllib.error.URLError as e:
                st.error(f"An error occurred: {e}")
            except Exception as e:  # Catch generic exceptions for unexpected errors
                st.error(f"Unexpected error: {e}")
            
    with col2:
        st.image('eleodora.jpeg')