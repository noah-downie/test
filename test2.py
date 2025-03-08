from openai import OpenAI
client = OpenAI(api_key="")
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a professio0nal triathalon coach."},
        {
            "role": "user",
            "content": "Do research on ironman training."
        }
    ]
)

print(completion.choices[0].message)