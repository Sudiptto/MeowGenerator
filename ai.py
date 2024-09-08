# For OpenAI function and developing the images
# this file contains all the AI related functions for jeapordy.py
from openai import AzureOpenAI, OpenAI
from passwords import *
from imgStorage import *
import os

# Set up API keys and client initialization
os.environ["OPENAI_API_KEY"] = OPENAI_4_KEY
client = OpenAI()

AOAI_ENDPOINT = AZURE_OPENAI_ENDPOINT
AOAI_KEY = AZURE_OPENAI_API_KEY
MODEL_NAME = "gpt-35-turbo"

openai_client = AzureOpenAI(
    api_key=AOAI_KEY,
    azure_endpoint=AOAI_ENDPOINT,
    api_version="2024-05-01-preview",
)

# Function to interact with OpenAI chat model
def OpenAIFunc(context, prompt):  
    response = openai_client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": f"{context}"},
            {"role": "user", "content": prompt}
        ],
        max_tokens=4000
    )
    ai_response = response.choices[0].message.content
    return ai_response

# Function to create an image prompt based on context and scene
def createImagePrompt(scene, context):
    img_prompt = (
        "Create a highly detailed and vivid image with the following characteristics: " 
        + context 
        + ". The scene should depict " + scene 
        + ". Maintain a consistent visual style across images by focusing on specific details such as a unified color palette, textures, and lighting. Ensure the use of consistent objects, character designs, and poses. Pay attention to recurring themes, the overall atmosphere, and a coherent setting that aligns with the context provided. Use similar background elements, lighting effects (such as natural sunlight or shadows), and ensure that the composition aligns with the style of previous images. "
        "Avoid randomness or variations that stray from the context. Keep the theme, visual style, and mood consistent to ensure continuity across multiple images in the same series."
    )

    image_url = generateImage(img_prompt)
    cloudImageUrl = getNewURL(image_url)
    
    return cloudImageUrl

# Function to get new URL -> from the IMGBB cloud server
def getNewURL(image_url):
    new_image_url = upload_image_to_imgbb(image_url, imgBBAPIKey)
    return new_image_url

# Function to generate images using OpenAI's DALL-E model
def generateImage(img_prompt):
    
    response = client.images.generate(
        model="dall-e-3",
        prompt=img_prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )
    image_url = response.data[0].url
    print(image_url)
    return image_url