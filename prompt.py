# Generating the story prompts / script and splitting up the script into n parts


# Generate story prompt function, view good prompt example in this file promptEx.txt
# Ayen section

import json
from ai import *
import re  # Import regular expressions library
from storage import *
from videoCreate import *

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

    # generate URLS -> ARRAy
    generatedUrls = send_Prompts(scenes, context)

    # generate video function here  -> STRING
    generatedVideoUrl = generateVideo(generatedUrls)

    # Create the JSON Data
    createdStory = createJSON(storyTitle, scenes, generatedUrls, emotion, generatedVideoUrl)

    return createdStory






# send prompts over and than get the image URLs
def send_Prompts(scenes, context):
    # End goal generate array of images url like this:
    # [image1.com, image2.com, image3.com...]
    
    #print(scenes, context)

    image_urls = []

    for scene in scenes:
        imageUrl = createImagePrompt(scene, context)
        image_urls.append(imageUrl)
    
    return image_urls



# Test cases to validate dynamic generation
def test_generate_story_prompt():
    # Test data
    storyTitle = "The Happy Fluffy Cat"
    catDescription = """
    Timmy: A chubby, playful orange cat who is always happy.
    Dragoon: A cat dragon
    Cupcake: Timmy’s father, a large orange cat with a more reserved and thoughtful demeanor."""

    emotion = "Happy"
    inspirationStory = "The scenes take place on a lovely day in the park, with an ice cream truck as a central focal point and Timmy's dragon cat friend Dragoon came and Dragoon playfully attacks timmy"
    parts = 2

    # Call the function with test data
    formatted_story = generate_story_prompt(storyTitle, catDescription, emotion, inspirationStory, parts)

    print(formatted_story)

if __name__ == "__main__":
    # Run test cases
    test_generate_story_prompt()
