import sys
import os
from dotenv import load_dotenv
load_dotenv()

sys.path.insert(0, os.path.dirname(__file__))
from lib_messaging import add_user_message, add_assistant_message, chat, client, model 

system_prompt = """
You are a patient math tutor.
Do not directly answer a student's questions.
Guide them to a solution step by step.
"""

messages = []

add_user_message(messages, "How do I solve the equation 5x + 3 = 2 for x?")

# answer = chat(messages)
answer = chat(messages, system_prompt=system_prompt)

print(answer)
