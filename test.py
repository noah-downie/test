import os
from openai import OpenAI

# Properly instantiate the OpenAI client
client = OpenAI(api_key='')

# Example function to interact with OpenAI API
def get_openai_response(prompt):
    response = client.completions.create(engine="text-davinci-003",
    prompt=prompt,
    max_tokens=150)
    return response.choices[0].text.strip()

# Test the setup
print("OpenAI API key loaded successfully!")

