import sys
import os
from dotenv import load_dotenv
load_dotenv()

sys.path.insert(0, os.path.dirname(__file__))
from lib_messaging import add_user_message, add_assistant_message, chat, client, model 

messages = []

add_user_message(messages, "Write a 1 sentence description of a fake database")

# stream = client.messages.create(
#     messages=messages, 
#     max_tokens=1000, 
#     model=model, 
#     stream=True)
# for chunk in stream:
#     print("----")
#     print("type :", type(chunk).__name__)
#     print("chunk:", chunk)

with client.messages.stream(
    model=model,
    messages=messages,
    max_tokens=1000
) as stream:
    for chunk in stream.text_stream:
        print(chunk, end="", flush=True)

# ) as stream:
#     for chunk in stream.text_stream:
#         pass
# print("Done!", stream.get_final_message().content[0].text)
