# For storing the JSON 
import json

# Function to create and update a JSON file with story data
def createJSON(storyTitle, scenes, imageURLs, emotion):
    file_name = "storyData.json"
    
    # Load existing data from the JSON file if it exists, otherwise start with an empty structure
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"Emotions": {}}
    
    # Check if the emotion already exists in the data
    if emotion not in data['Emotions']:
        data['Emotions'][emotion] = []
    
    # Check if the storyTitle already exists in the emotion category
    story_exists = check_story_exists(data, emotion, storyTitle)
    
    # If the storyTitle does not exist, create a new entry for the story
    if not story_exists:
        new_story = create_new_story(storyTitle, scenes, imageURLs)
        data['Emotions'][emotion].append(new_story)
    else:
        add_scenes_to_story(data, emotion, storyTitle, scenes, imageURLs)
    
    # Save the updated data back to the JSON file
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=2)

# Function to check if a story already exists in the data
def check_story_exists(data, emotion, storyTitle):
    for story in data['Emotions'][emotion]:
        if story['Story Title'] == storyTitle:
            return True
    return False

# Function to create a new story entry
def create_new_story(storyTitle, scenes, imageURLs):
    new_story = {
        'Story Title': storyTitle,
        'script': []
    }
    for i in range(len(scenes)):
        new_story['script'].append({
            'Scene': scenes[i],
            'Image URL': imageURLs[i]
        })
    return new_story

# Function to add scenes to an existing story
def add_scenes_to_story(data, emotion, storyTitle, scenes, imageURLs):
    for story in data['Emotions'][emotion]:
        if story['Story Title'] == storyTitle:
            for i in range(len(scenes)):
                story['script'].append({
                    'Scene': scenes[i],
                    'Image URL': imageURLs[i]
                })
            break


# function to erase the storyData.json
def eraseJSON():
    file_name = "storyData.json"
    data = {"Emotions": {}}
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=2)


# Example usage:
scenes = [
    "Timmy, a chubby, playful orange cat, and his father Cupcake, a large black cat with a more reserved and thoughtful demeanor, frolic in the park on a sunny day. The grass is a vibrant green, sprinkled with delicate dandelions that sway in the gentle breeze. The park is filled with children laughing and playing, their delightful giggles echoing through the air. Timmy chases after butterflies, his tail flicking with excitement, as Cupcake watches on with a contented smile. In the distance, the melodic tune of an ice cream truck beckons, promising sweet treats and smiles.",
    "Timmy's eyes light up with joy as the ice cream truck comes into view. The truck, adorned with colorful illustrations of scoops and sundaes, is surrounded by a crowd of eager kids. The truck's frozen delights glisten in the sun, tempting every passerby. Timmy and Cupcake join the line, their anticipation growing with each scoop of ice cream served. The sound of laughter and blissful sighs fill the air as children indulge in the delicious treats. Timmy, with a drippy vanilla cone in his paw, bounces up and down with excitement, his happiness contagious.",
    "As the sun begins to set, casting a warm orange glow across the park, Timmy and Cupcake find a cozy spot under a towering oak tree. The air is filled with a peaceful serenity as the sounds of nature soothe their souls. Timmy purrs contentedly, his belly full and his heart brimming with joy. Cupcake leans against Timmy, gently grooming his fur, their bond evident in their every action. The day draws to a close, but the memories of their adventures in the park and the taste of sweet ice cream linger, leaving both Timmy and Cupcake with a sense of everlasting happiness."
]

imageURLs = [
    "https://oaidalleapiprodscus.blob.core.windows.net/private/org-imNaN6rEUdKXOnqsH3Qc6tMg/user-ekqgja6dmFIdPEH07QgYdF8X/img-lyBny15caUtnIsbWePlSkdab.png?st=2024-09-07T15%3A25%3A48Z&se=2024-09-07T17%3A25%3A48Z&sp=r&sv=2024-08-04&sr=b&rscd=inline&rsct=image/png&skoid=d505667d-d6c1-4a0a-bac7-5c84a87759f8&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-09-06T21%3A48%3A51Z&ske=2024-09-07T21%3A48%3A51Z&sks=b&skv=2024-08-04&sig=7Ulbp4hUzBhT7vToTTCw0gnSHaVieWZLVffIrD%2B8lno%3D",
    "https://oaidalleapiprodscus.blob.core.windows.net/private/org-imNaN6rEUdKXOnqsH3Qc6tMg/user-ekqgja6dmFIdPEH07QgYdF8X/img-exJKzokrFAA6UJwANagVSVFa.png?st=2024-09-07T15%3A26%3A07Z&se=2024-09-07T17%3A26%3A07Z&sp=r&sv=2024-08-04&sr=b&rscd=inline&rsct=image/png&skoid=d505667d-d6c1-4a0a-bac7-5c84a87759f8&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-09-06T21%3A25%3A40Z&ske=2024-09-07T21%3A25%3A40Z&sks=b&skv=2024-08-04&sig=KSuQqBFtQEIrId5qZRyL9A6arh7a%2B/OFYvPF53TtJ88%3D",
    "https://oaidalleapiprodscus.blob.core.windows.net/private/org-imNaN6rEUdKXOnqsH3Qc6tMg/user-ekqgja6dmFIdPEH07QgYdF8X/img-pePD8kLiQJ8Q0dFTgaoOmw2f.png?st=2024-09-07T15%3A26%3A20Z&se=2024-09-07T17%3A26%3A20Z&sp=r&sv=2024-08-04&sr=b&rscd=inline&rsct=image/png&skoid=d505667d-d6c1-4a0a-bac7-5c84a87759f8&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-09-06T22%3A11%3A19Z&ske=2024-09-07T22%3A11%3A19Z&sks=b&skv=2024-08-04&sig=%2BUUs553UNQDRqILXRSH7WMLQln4z9yMDsahso7oaD8g%3D"
]

#createJSON("The Ice Cream Office Scene", scenes, imageURLs, "Mad")
eraseJSON()