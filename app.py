import os   
from openai import OpenAI




endpoint = "https://shant-mjjz4han-eastus2.cognitiveservices.azure.com/openai/v1"  # Replace with your actual endpoint URL
deployment_name = "gpt-4o-standard"


# Read ENV
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")


client = OpenAI(
    base_url=endpoint,
    api_key = AZURE_OPENAI_API_KEY
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
