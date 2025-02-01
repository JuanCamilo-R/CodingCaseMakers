from app.env import ENV_VARIABLES
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", api_key=ENV_VARIABLES["OPENAI_API_KEY"], temperature=0.5)