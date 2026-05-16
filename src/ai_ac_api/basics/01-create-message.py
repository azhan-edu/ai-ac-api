# Install dependencies
# %pip install anthropic python-dotenv
# uv pip install anthropic python-dotenv
# source .venv/bin/activate

# Load env variables
from dotenv import load_dotenv
load_dotenv()

# Create an API client
from anthropic import Anthropic
client = Anthropic()
model = "claude-sonnet-4-6"

# Make a request
message = client.messages.create(
  model=model, max_tokens=1000, messages=[
    {  
      "role": "user",
      "content": "What is quantum computing? Answer in one sentence"
    }
  ]
)
print (message.content[0].text)