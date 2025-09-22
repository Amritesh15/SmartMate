from fastapi import FastAPI, Form
from fastapi.responses import PlainTextResponse
from nodes.gpt_node import GPTNode
from nodes.calendar_node import CalendarNode
from utils import send_whatsapp_message
import os

app = FastAPI()

gpt_node = GPTNode()
calendar_node = CalendarNode()

@app.post("/webhook")
async def whatsapp_webhook(From: str = Form(...), Body: str = Form(...)):
    print(f"Incoming message from {From}: {Body}")

    # 1️⃣ Interpret with GPT
    intent_data = gpt_node.process(Body)

    # 2️⃣ Route to appropriate node
    action = intent_data.get("action")
    if action in ["add_event", "list_events", "delete_event"]:
        reply = calendar_node.process(intent_data)
    else:
        reply = f"I understood your message: {intent_data.get('raw', Body)}"

    # 3️⃣ Reply via WhatsApp
    send_whatsapp_message(From, reply)
    return PlainTextResponse("OK")
