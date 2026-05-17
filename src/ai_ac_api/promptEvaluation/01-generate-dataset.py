import json
import sys
import os
from dotenv import load_dotenv
load_dotenv()

sys.path.insert(0, os.path.dirname(__file__))
from lib_messaging import add_user_message, add_assistant_message, chat, client, model 

def generate_dataset():
  prompt = """
    Generate an evaluation dataset for a prompt evaluation. The dataset will be used to evaluate prompts that generate Python, JSON, or Regex specifically for AWS-related tasks. Generate an array of JSON objects, each representing task that requires Python, JSON, or a Regex to complete.

    Example output:
    ```json
    [
      {
        "task": "Description of task",
        "format": "python | json | regex",
        "solution_criteria": "Key criteria for evaluating the solution"
      },
      ...additional
    ]
    ```

    * Focus on tasks that can be solved by writing a single Python function, a single JSON object, or a single regex
    * Focus on tasks that do not require writing much code

    Please generate 3 objects.
  """

  messages = []
  add_user_message(messages, prompt)
  add_assistant_message(messages, "```json")
  text = chat(messages, stop_sequences=["```"])
  return json.loads(text)

tasks = generate_dataset()

# tasks = [
#   { "task": "Create a Python function to extract the AWS region from an ARN (Amazon Resource Name)" },
#   { "task": "Write a JSON configuration for an AWS Lambda function that defines basic environment variables and memory settings"},
#   { "task": "Develop a regular expression to validate an AWS S3 bucket name (lowercase, alphanumeric, between 3-63 characters)"}
# ]

with open(os.path.join(os.path.dirname(__file__), "data_set.json"), "w") as f:
  json.dump(tasks, f, indent=2) 