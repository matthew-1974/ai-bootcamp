from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()   # reads .env
client = OpenAI()   
MODEL = 'gpt-5.4-nano'
response = client.responses.create(
    model = MODEL,
    instructions = "You are an aggresive Python tutor.",
    input = 'Explain what a dictionary is in 3 sentences.',
)

print(response.output_text)
print(response.usage)
