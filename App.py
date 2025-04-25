from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
load_dotenv()
API_KEY=os.getenv("GROQ_API_KEY")
LLM=ChatGroq(model="llama-3.3-70b-versatile", api_key=API_KEY)
#interact with LLM
inputs=input("you:")
response=LLM.invoke(inputs)
print(response.content)