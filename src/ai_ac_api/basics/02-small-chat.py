import sys
import os
from dotenv import load_dotenv
load_dotenv()

sys.path.insert(0, os.path.dirname(__file__))
from lib_messaging import add_user_message, add_assistant_message, chat

messages = []
while True:
  # Get user input
  user_input = input("> ")
  print(">", user_input)
  # Add user input to the list of messages
  add_user_message(messages, user_input)
  # Call Claude with the 'chat' function
  answer = chat(messages)
  # Add generated text to the list of messages
  add_assistant_message(messages, answer)
  # Print the generated text
  print("—-_")
  print(answer)
  print("---")
