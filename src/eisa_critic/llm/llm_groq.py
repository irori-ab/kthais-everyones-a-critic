
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate


def chat(messages, groq_api_key): 
    client = ChatGroq(
        model="openai/gpt-oss-120b",
        temperature=0,
        max_tokens=None,
        reasoning_format="parsed",
        timeout=None,
        max_retries=2,
        api_key=groq_api_key
        # other params...
    )

    return client.invoke(messages)
