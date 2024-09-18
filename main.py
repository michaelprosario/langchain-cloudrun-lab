import os

google_api_key = os.environ["GOOGLE_API_KEY"]


from fastapi import FastAPI
from langchain import hub
from langchain_chroma import Chroma
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_google_genai import GoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langserve import add_routes

llm = GoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=google_api_key)

system_template = "Respond as Mr. Spock from Star Trek:"
prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)

rag_chain = (
    prompt_template
    | llm
    | StrOutputParser()
)

from fastapi import FastAPI
from langserve import add_routes

# App definition
app = FastAPI(
  title="LangChain Server",
  version="1.0",
  description="A simple API server using LangChain's Runnable interfaces",
)

# Adding chain route
add_routes(
    app,
    rag_chain,
    path="/chain",
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=80)
