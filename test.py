from load_dotenv import load_dotenv
load_dotenv()
from openai import OpenAI




endpoint = "endpoint_url_here"  # Replace with your actual endpoint URL
deployment_name = "gpt-4o-standard"


client = OpenAI(
    base_url=endpoint
)

# Read the system prompt from an external file
with open("system.promp.txt", "r") as file:
    system_prompt = file.read().strip() 

completion = client.chat.completions.create(
    model=deployment_name,
    messages=[
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": "who is prime minister of INDIA?"
        }
    ],
)

print(completion.choices[0].message)