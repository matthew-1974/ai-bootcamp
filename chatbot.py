from dotenv import load_dotenv
from pathlib import Path

from openai import OpenAI
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(env_path, override=True)

client = OpenAI()
MODEL = 'gpt-5.4-nano'
SYSTEM = "You are a serious movie lover who spends most of the time in Letterboxd and loves talking about niche moives"

history = []

while True:
    user_text = input('You: ')
    if user_text.lower() in ('quit', 'exit'):
        break
    history.append({"role": "user", "content": user_text})
    response = client.responses.create(model=MODEL, instructions=SYSTEM, input=history)
    answer = response.output_text
    history.append({"role": "assistant", "content": answer})
    print("Bot:", answer)