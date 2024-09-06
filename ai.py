# For OpenAI function and developing the images
# this file contains all the AI related functions for jeapordy.py
from openai import AzureOpenAI
from passwords import *

#Setting up AI
AOAI_ENDPOINT = AZURE_OPENAI_ENDPOINT
AOAI_KEY = AZURE_OPENAI_API_KEY 
MODEL_NAME = "gpt-35-turbo"

openai_client = AzureOpenAI(
    api_key=AOAI_KEY,
    azure_endpoint=AOAI_ENDPOINT,
    api_version="2024-05-01-preview",
)

#context -> context of the conversation
#prompt -> the user's input
def OpenAIFunc(context, prompt):
    response = openai_client.chat.completions.create(
                model=MODEL_NAME,
                messages=[
                    {"role": "system", "content": f"{context}"} ,
                    {"role": "user", "content":prompt}
                ],
                max_tokens=4000
            )
    ai_response = (response.choices[0].message.content)

    return ai_response


# Function to generate images from text'
# Context consists of setting, cat description 

# Samin's part
def generateImage(scene, context):
    pass