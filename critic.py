
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

    if ("messages" not in st.session_state) or len(st.session_state) == 1:
        st.session_state["messages"] = [{"role": "assistant", "content": "I will provide feedback on your writing"}]

    if "harshness" not in st.session_state:
        st.session_state["harshness"] = "encouraging"


    st.radio("Critique mode:", ["encouraging", "constructive", "harsh"], key="harshness")

    st.write("You've selected harshness:", st.session_state.harshness)


    groq_api_key = st.secrets.groq_api_key

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    if prompt := st.chat_input():
        if not groq_api_key.startswith("gsk_"):
            st.info("Missing valid Groq key in Streamlit secrets")
            st.stop()

        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)

        system_prompt = "You provide {harshness} feedback on writing, considering tone, style and grammar".format(harshness=st.session_state.harshness)
        system_message = {"role": "system", "content": system_prompt}
        
        # debug print:
        # st.write("System prompt: ", system_prompt)

        response = llm_groq.chat([system_message] + st.session_state.messages, groq_api_key)

        msg = response.content

        st.session_state.messages.append({"role": "assistant", "content": msg})

        st.chat_message("assistant").write(msg)


if __name__ == "__main__":
    main()
