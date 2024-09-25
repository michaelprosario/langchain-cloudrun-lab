import os

from fastapi.responses import HTMLResponse

google_api_key = os.environ["GOOGLE_API_KEY"]

from fastapi import FastAPI
from langchain import hub

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import GoogleGenerativeAI
from langserve import add_routes

llm = GoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=google_api_key)

system_template = "Respond as Professor Albus Dumbledore from Harry Potter:"
prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)

bot_chain = (
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
    bot_chain,
    path="/chain",
)

# read the index.html file
@app.get("/")
def read_root():
    html = ""
    with open("index.html", "r") as f:
        html = f.read()
    return HTMLResponse(content=html, status_code=200)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=80)
