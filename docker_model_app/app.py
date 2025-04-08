import streamlit as st
import requests

API_URL = "http://localhost:8000/engines/llama.cpp/v1/chat/completions"

st.set_page_config(page_title="LLM Chat powered by Docker Model Runner", page_icon=":robot_face:")
st.title("LLM Chat")
st.caption("This app is powered by Docker Model Runner")


if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "あなたは優秀なアシスタントです．"}
    ]

for msg in st.session_state.messages[1:]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("メッセージを入力...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    with st.chat_message("user"):
        st.markdown(user_input)
    
    headers = {"Content-Type": "application/json"}
    data = {
        "model": "ai/mistral",
        "messages": st.session_state.messages
    }

    try:
        response = requests.post(API_URL, headers=headers, json=data)
        response.raise_for_status()
        data = response.json()

        assistant_reply = data["choices"][0]["message"]["content"]
    except Exception as e:
        assistant_reply = f"Error: {e}"
    
    st.session_state.messages.append({"role": "assistant", "content": assistant_reply})

    with st.chat_message("assistant"):
        st.markdown(assistant_reply)
