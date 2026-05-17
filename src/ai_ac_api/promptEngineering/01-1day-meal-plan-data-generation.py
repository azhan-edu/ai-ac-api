import json
from statistics import mean
import sys
import os
from dotenv import load_dotenv
load_dotenv()

sys.path.insert(0, os.path.dirname(__file__))
from lib_messaging import add_user_message, add_assistant_message, chat, client, model 
from lib_promptEvaluator import PromptEvaluator
from lib_reportBuilder import generate_prompt_evaluation_report

evaluator = PromptEvaluator(max_concurrent_tasks=1)

dataset_file_name = os.path.join(os.path.dirname(__file__), "data_set.json")

dataset = evaluator.generate_dataset(
    # Describe the purpose or goal of the prompt you're trying to test
    task_description="Write a compact, concise 1 day meal plan for a single athlete",
    # Describe the different inputs that your prompt requires
    prompt_inputs_spec={
        "age": "Athlete's age in years",
        "height": "Athlete's height in cm",
        "weight": "Athlete's weight in kg",
        "goal": "Goal of the athlete",
        "restrictions": "Dietary restrictions of the athlete",
    },
    # Where to write the generated dataset
    output_file=dataset_file_name,
    # Number of test cases to generate (recommend keeping this low if you're getting rate limit errors)
    num_cases=2,
)