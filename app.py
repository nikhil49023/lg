import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq 

load_dotenv() 

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature = 1.2
)
response = llm.invoke("confirm you are online and tell me your name in one sentence.")
print(response.content)