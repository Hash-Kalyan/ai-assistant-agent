
import os
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"]
)

memory = ConversationBufferMemory()
llm = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
conversation = ConversationChain(llm=llm, memory=memory)

@app.get("/")
def read_root():
    return {"message": "AI Personal Assistant is running!"}

@app.post("/query")
async def handle_query(request: Request):
    data = await request.json()
    user_input = data.get("message")
    response = conversation.predict(input=user_input)
    return {"response": response}
