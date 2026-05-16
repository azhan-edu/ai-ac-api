# Create an API client
from anthropic import Anthropic
client = Anthropic()
model = "claude-sonnet-4-6"

def add_user_message(messages, text):
    user_message = {"role": "user", "content": text}
    messages.append(user_message)

def add_assistant_message(messages, text):
    assistant_message = {"role": "assistant", "content": text}
    messages.append(assistant_message)

def chat(messages, system_prompt=None, temperature=1.0, stop_sequences=None):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
        "temperature": temperature
    }

    if system_prompt:
        params["system"] = system_prompt

    if stop_sequences:
        params["stop_sequences"] = stop_sequences

    print("Request parameters:", params)

    message = client.messages.create(**params)

    return message.content[0].text
