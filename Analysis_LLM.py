"""
# Author: Lee Taylor
Develop a tool to report in realtime the activities of any given company.
"""
import os
import openai
import api_key  # Create a file called
import pandas as pd
import csv
import time


# Load your API key from an environment variable or secret management service
openai.api_key = api_key.API_KEY


def create_prompt(paragraphs, user_topic=f'Write a bullet point list only '
                                    f'containing activities directly conducted by the company:'):
    # Form and return prompt as a string
    return f"{user_topic} {paragraphs}."


def gen_response(prompt):
    response = openai.Completion.create(model="text-davinci-003",
                                        prompt=prompt,
                                        temperature=0,
                                        max_tokens=2000)
    return response


def response_text(response):
    return response["choices"][0]["text"]


def print_fio(prompt, res):
    print(f"[BEGIN]\n"
          f"Me: {prompt}\n\n"
          f"text-davinci-003: {response_text(res).strip()}\n"
          f"[END]\n")


def write_to_csv(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as f:
        writer = csv.writer(f)
        for line in data:
            try:
                writer.writerow(line)
            except Exception as e:
                writer.writerow(['Failed', 'Failed', 'Failed', 'Failed', 'Failed'])


if __name__ == '__main__':
    pass
