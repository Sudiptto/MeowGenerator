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

    print("Updated JSON FILE")

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


#createJSON("The Ice Cream Office Scene", scenes, imageURLs, "Mad")
eraseJSON()