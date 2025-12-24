import os
from fastapi import FastAPI, Request
from pydantic import BaseModel
from openai import OpenAI

# Initialize FastAPI app
app = FastAPI()


# Define your endpoint, deployment name, and API key
endpoint = "https://shant-mjjz4han-eastus2.cognitiveservices.azure.com/openai/v1"  # Replace with your actual endpoint URL
deployment_name = "gpt-4o-standard"
# 
AZURE_OPENAI_API_KEY= os.getenv("AZURE_OPENAI_API_KEY)

# Initialize OpenAI client
client = OpenAI(
    base_url=endpoint,
    api_key=AZURE_OPENAI_API_KEY
)

@app.get("/")
def root():
    return{"status": "running"}
    
# Read the system prompt from an external file
with open("system.promp.txt", "r") as file:
    system_prompt = file.read().strip()

# Define a Pydantic model for the request body
class ChatRequest(BaseModel):
    user_input: str

# Create the /chat endpoint
@app.post("/chat")
async def chat(request: ChatRequest):
    user_input = request.user_input  # Extract user input from the request body

    # Create the chat completion request
    completion = client.chat.completions.create(
        model=deployment_name,
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_input
            }
        ],
    )

    # Return the assistant's response
    return {"response": completion.choices[0].message.content}


