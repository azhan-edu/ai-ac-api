import sys
import os
from dotenv import load_dotenv
load_dotenv()

sys.path.insert(0, os.path.dirname(__file__))
from lib_messaging import add_user_message, add_assistant_message, chat, client, model 

messages = []

# add_user_message(messages, "Count from 1 to 10")
# text = chat(messages, stop_sequences=["5", "3, 4"])

add_user_message(messages, "Generate a very short event bridge rule as json")

# text = chat(messages)
# print(text)
# response
# Here's a simple EventBridge rule in JSON:
# ```json
# {
#   "source": ["aws.ec2"],
#   "detail-type": ["EC2 Instance State-change Notification"],
#   "detail": {
#     "state": ["stopped"]
#   }
# }
# ```

add_assistant_message(messages, "```json")
text = chat(messages, stop_sequences=["```"])

print(text)
import json

print(json.loads(text))


# This tells Claude "start your response with ```json" and then stop before the closing fence, giving you clean JSON. It worked on Claude 3 models.
# Claude 4 (including claude-sonnet-4-6) removed support for prefill. The API now rejects any request where the last message has role: "assistant".
# The alternatives:
# Explicit instruction — tell Claude to respond with raw JSON only (simplest)
# System prompt — set system="Respond only with valid JSON, no markdown"
# Strip the fences in code — let Claude wrap in ```json ``` and parse it out yourself
