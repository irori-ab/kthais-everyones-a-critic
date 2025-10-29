
import streamlit as st
import os

from eisa_critic.llm import llm_groq

def main():
    st.markdown(
    r"""
    <style>
    .stAppDeployButton {
            visibility: hidden;
        }
    </style>
    """, unsafe_allow_html=True)

    st.title("Everyone's a critic")

    groq_api_key = st.secrets.groq_api_key

    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    if prompt := st.chat_input():
        if not groq_api_key.startswith("gsk_"):
            st.info("Please add your Groq API key to continue.")
            st.stop()

        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)

        response = llm_groq.chat(st.session_state.messages, groq_api_key)

        msg = response.content

        st.session_state.messages.append({"role": "assistant", "content": msg})

        st.chat_message("assistant").write(msg)


if __name__ == "__main__":
    main()
