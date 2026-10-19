
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(env_path, override=True)

client = OpenAI()

MODEL = "gpt-5.4-nano"

response = client.responses.create(
    model=MODEL,
    instructions="You are a strict but helpful Python tutor.",
    input="Explain what a dictionary is in 3 sentences.",
)

print(response.output_text)
print(response.usage)
