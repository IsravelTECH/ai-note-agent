import os
from dotenv import load_dotenv
from openai import OpenAI

from explorer import explore_repo
from planner import create_plan
from summarizer import summarize

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

request = "Improve the application so users can better organise and search their notes."

context = explore_repo("./node-easy-notes-app")
plan = create_plan(context, request)

print("Relevant files found:")
for f in context["files"][:10]:
    print("-", f)

print()
summarize(plan)

response = client.chat.completions.create(
    model="openai/gpt-oss-20b:free",
    messages=[
        {"role": "system", "content": "You are an AI coding agent."},
        {"role": "user", "content": request}
    ]
)

print("\nLLM suggestion:\n")
print(response.choices[0].message.content)