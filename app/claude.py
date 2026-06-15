from dotenv import load_dotenv
from anthropic import Anthropic
import os
import json
load_dotenv()
client=Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
model='claude-haiku-4-5-20251001'

def add_user_message(messages,text):
    user_message={"role": "user" , "content": text}
    messages.append(user_message)

def add_assistant_message(messages,text):
    assistant_message={"role": "assistant" , "content": text}
    messages.append(assistant_message)

def chat(messages):
    message=client.messages.create(
        model=model ,
        max_tokens=1000,
        messages=messages,
    )
    return message.content[0].text

