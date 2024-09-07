# For OpenAI function and developing the images
# this file contains all the AI related functions for jeapordy.py
from openai import AzureOpenAI, OpenAI
from passwords import *
import os 

#openAI key to use dalle-3 to generate images
os.environ["OPENAI_API_KEY"] = OPENAI_4_KEY
client = OpenAI()

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
# ex. 
# scene @return: A string of a description of a scene   
def generateImage(scene, context):
    img_prompt = "Knowing that " +context + ", then create an image of " +scene
    client = OpenAI()
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


"""context = "context"
scene = "scene"
prompt = "Knowing that "+context +", then create an image of " +scene
print(prompt)"""

generateImage("Timmy, now standing in front of the ice cream truck, is mesmerized by the colorful array of ice creams displayed in the window. The truck's bell jingles occasionally as customers come and go. Timmy’s paws press against the counter, and his nose twitches with excitement. Cupcake stands beside him, holding Timmy’s favorite flavor in his hand but with a pensive look in his eyes. The mood subtly shifts as Cupcake looks around the park, noting its quiet solitude despite the sunny weather.", "Timmy: A chubby, playful orange cat who is always happy. Cupcake: Timmy’s father, a large black cat with a more reserved and thoughtful demeanor. Setting: The scenes take place on a lovely day in the park, with an ice cream truck as a central focal point." )