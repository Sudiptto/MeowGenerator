# Generating the story prompts / script and splitting up the script into n parts


# Generate story prompt function, view good prompt example in this file promptEx.txt
# Ayen section

import json
from ai import *
import re  # Import regular expressions library
from storage import *

# Function to dynamically generate a story prompt
def generate_story_prompt(storyTitle, catDescription, emotion, inspirationStory, parts):
    # Construct the prompt dynamically
    prompt = f"""
    I am writing an in-depth, multi-part script that will be divided into '{parts}' scenes. Each scene must be vividly descriptive, as the purpose of this script is to serve as a blueprint for creating visual illustrations, later to be used in an image-generating AI. Therefore, I need each scene to be rich in detail, focusing on mood, setting, and character actions. The script is also meant for teens and kids, leaving them in awe. Each scene should be concise—only one paragraph per scene.

    The format of the script should strictly follow this structure:

    Story Title: {storyTitle}

    Scene 1:
    [Detailed text]

    Scene 2:
    [Detailed text]

    ...

    Scene {parts}:
    [Detailed text]

    The core elements of the story are as follows:

    Emotion: {emotion}
    Character description: {catDescription}
    Setting: {inspirationStory}
    Total Parts: The story should consist of {parts} scenes.

    This is a completely original story, not inspired by any existing works. Please provide the script formatted exactly as requested.
    """

    # Call the OpenAI function with the generated prompt and store the response
    response = OpenAIFunc("You are a story generator.", prompt)
    #print(response)

    # Use regex to split the response into scenes based on the pattern "Scene X:"
    scenes = re.findall(r"Scene \d+:(.*?)(?=Scene \d+:|$)", response, re.DOTALL)
    scenes = [scene.strip() for scene in scenes if scene.strip()]

    
    # Check if the number of scenes matches the expected number
    if len(scenes) != parts:
        print(f"Warning: Expected {parts} scenes, but found {len(scenes)} scenes.")

    context = catDescription + "  "  + inspirationStory
    send_Prompts(scenes, storyTitle, context, emotion)



def send_Prompts(scenes, storyTitle, context, emotion):
    # End goal generate array of images url like this:
    # [image1.com, image2.com, image3.com...]
    
    #print(scenes, context)

    image_urls = ['https://oaidalleapiprodscus.blob.core.windows.net/private/org-imNaN6rEUdKXOnqsH3Qc6tMg/user-ekqgja6dmFIdPEH07QgYdF8X/img-meuNxBZKAV7HEjIk6nUH7Ipw.png?st=2024-09-07T16%3A51%3A09Z&se=2024-09-07T18%3A51%3A09Z&sp=r&sv=2024-08-04&sr=b&rscd=inline&rsct=image/png&skoid=d505667d-d6c1-4a0a-bac7-5c84a87759f8&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-09-07T00%3A08%3A11Z&ske=2024-09-08T00%3A08%3A11Z&sks=b&skv=2024-08-04&sig=TPvZKBnmH4YPqxphl%2B%2B21jfgcgwJ8glLS1Ch/pcEhmg%3D', 'https://oaidalleapiprodscus.blob.core.windows.net/private/org-imNaN6rEUdKXOnqsH3Qc6tMg/user-ekqgja6dmFIdPEH07QgYdF8X/img-TjYmwLa5CHEXTSX1ruGHo3Ti.png?st=2024-09-07T16%3A51%3A24Z&se=2024-09-07T18%3A51%3A24Z&sp=r&sv=2024-08-04&sr=b&rscd=inline&rsct=image/png&skoid=d505667d-d6c1-4a0a-bac7-5c84a87759f8&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-09-07T06%3A45%3A58Z&ske=2024-09-08T06%3A45%3A58Z&sks=b&skv=2024-08-04&sig=JZpHMEZt4Y3Xy3a0vY2GazK9ywqMcnu2U/VfgVU2IJE%3D', 'https://oaidalleapiprodscus.blob.core.windows.net/private/org-imNaN6rEUdKXOnqsH3Qc6tMg/user-ekqgja6dmFIdPEH07QgYdF8X/img-YG0zpcbhVFd3IojyQ7mPwTkH.png?st=2024-09-07T16%3A51%3A41Z&se=2024-09-07T18%3A51%3A41Z&sp=r&sv=2024-08-04&sr=b&rscd=inline&rsct=image/png&skoid=d505667d-d6c1-4a0a-bac7-5c84a87759f8&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-09-06T23%3A26%3A50Z&ske=2024-09-07T23%3A26%3A50Z&sks=b&skv=2024-08-04&sig=hR1rJWnpXP2sKiRDIEw3LUmoOTXYfa4%2BqZXSPDbVZbA%3D']

    """for scene in scenes:
        imageUrl = createImagePrompt(scene, context)
        image_urls.append(imageUrl)"""
    
    #print(image_urls)

    createJSON(storyTitle, scenes, image_urls, emotion)


# Test cases to validate dynamic generation
def test_generate_story_prompt():
    # Test data
    storyTitle = "The Doge and The Cat"
    catDescription = """
    Timmy: A chubby, playful orange cat who is always happy.
    Cupcake: Timmy’s father, a large orange cat with a more reserved and thoughtful demeanor."""

    emotion = "Sad"
    inspirationStory = "The scenes take place on a lovely day in the park, with an ice cream truck as a central focal point."
    parts = 3

    # Call the function with test data
    formatted_story = generate_story_prompt(storyTitle, catDescription, emotion, inspirationStory, parts)

    print(formatted_story)

if __name__ == "__main__":
    # Run test cases
    test_generate_story_prompt()
