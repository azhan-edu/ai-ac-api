import json
from statistics import mean
import sys
import os
from dotenv import load_dotenv
load_dotenv()

sys.path.insert(0, os.path.dirname(__file__))
from lib_messaging import add_user_message, add_assistant_message, chat, client, model 

def run_prompt(test_case):
  """Merges the prompt and test case input, then returns the result"""
  prompt = f"""
    Please solve the following task:
    {test_case["task"]}
  """

  messages = []
  add_user_message(messages, prompt)
  output = chat(messages)
  return output

def grade_by_model(test_case, output):
    eval_prompt = f"""
      You are an expert AWS code reviewer. Your task is to evaluate the following AI-generated solution.

      Original Task:
      <task>
      {test_case["task"]}
      </task>

      Solution to Evaluate:
      <solution>
      {output}
      </solution>

      Output Format
      Provide your evaluation as a structured JSON object with the following fields, in this specific order:
      - "strengths": An array of 1-3 key strengths
      - "weaknesses": An array of 1-3 key areas for improvement
      - "reasoning": A concise explanation of your overall assessment
      - "score": A number between 1-10

      Respond with JSON. Keep your response concise and direct.
      Example response shape:
      {{
          "strengths": string[],
          "weaknesses": string[],
          "reasoning": string,
          "score": number
      }}
    """

    messages = []
    add_user_message(messages, eval_prompt)
    add_assistant_message(messages, "```json")
    eval_text = chat(messages, stop_sequences=["```"])
    return json.loads(eval_text)

def run_test_case(test_case):
  """Calls run_prompt, then grades the result"""
  output = run_prompt(test_case)
  
  model_grade = grade_by_model(test_case, output)
  score = model_grade["score"]
  reasoning = model_grade["reasoning"]
  
  return {
      "output": output,
      "test_case": test_case,
      "score": score,
      "reasoning": reasoning,
  }

def run_eval(dataset):
  """Loads the dataset and calls run_test_case with each case"""
  results = []
  
  for test_case in dataset:
      result = run_test_case(test_case)
      results.append(result)
  
  average_score = mean([result["score"] for result in results])
  print(f"Average score: {average_score}")

  return results


with open(os.path.join(os.path.dirname(__file__), "data_set.json"), "r") as f:
  tasks = json.load(f)

results = run_eval(tasks)
print(json.dumps(results, indent=2))
