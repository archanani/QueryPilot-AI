from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
load_dotenv()
llm = ChatGroq(
    model=os.getenv("MODEL"),
    groq_api_key=os.getenv("GROQ_API_KEY"),
    temperature=0
)

