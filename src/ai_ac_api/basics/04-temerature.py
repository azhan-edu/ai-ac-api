import sys
import os
from dotenv import load_dotenv
load_dotenv()

sys.path.insert(0, os.path.dirname(__file__))
from lib_messaging import add_user_message, add_assistant_message, chat, client, model 

messages = []

add_user_message(messages, "Generate a one sentence movie idea.")

answer = chat(messages, temperature=0.9)

print(answer)
