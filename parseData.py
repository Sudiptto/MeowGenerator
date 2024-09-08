# Used to parse data from the storyData.json file and return the data in the JSON format
import json

# Load your JSON data
with open('storyData.json') as f:
    story_data = json.load(f)

# Function returns all JSON DATA from storyData.json
def get_all_data():
    return json.dumps(story_data, indent=4)

# query the JSON data via emotion
def query_stories_by_emotion(emotion):
    emotions = story_data.get("Emotions", {})

    # Check if the emotion exists
    if emotion in emotions:
        return json.dumps(emotions[emotion], indent=4)
    else:
        return json.dumps({"error": "Emotion not found"}, indent=4)
    

# Function to query the JSON data via story title, checking across all emotions
def query_story_by_title(story_title):
    # Loop through all emotions in the data
    for emotion, stories in story_data.get('Emotions', {}).items():
        # Loop through each story in the current emotion
        for story in stories:
            if story.get('Story Title') == story_title:
                return json.dumps(story, indent=4)

    # If no story is found, return an error
    return json.dumps({"error": "Story not found"}, indent=4)

# Function to query stories based on the number of parts (length of the "script" array)
def query_stories_by_parts(parts):
    matching_stories = []

    # Loop through all emotions
    for emotion, stories in story_data.get('Emotions', {}).items():
        # Loop through each story under the emotion
        for story in stories:
            # Check the length of the "script" field
            if len(story.get('script', [])) == parts:
                # Add matching story to the results
                matching_stories.append(story)
    
    # If no stories match the number of parts, return an error
    if not matching_stories:
        return json.dumps({"error": "No stories found with the specified number of parts"}, indent=4)
    
    # Return all matching stories
    return json.dumps(matching_stories, indent=4)

# Function to query based on emotion and story title
def query_story_by_emotion_and_title(emotion, story_title):
    # First check if the emotion exists using the previous function
    emotion_data = query_stories_by_emotion(emotion)

    # If emotion not found, return error
    if "error" in emotion_data:
        return json.dumps({"error": "Emotion not found"}, indent=4)
    
    # if story not found, return error
    if "error" in query_story_by_title(story_title):
        return json.dumps({"error": "Story not found"}, indent=4)

    # Now search for the story title in the emotion data

    for story in story_data['Emotions'][emotion]:
        if story['Story Title'] == story_title:
            return json.dumps(story, indent=4)

    # If the story title is not found, return an error
    return json.dumps({"error": "Story not found"}, indent=4)





# Example usage
#emotion = "Happy"  # Replace with the emotion you want to query
#story_title = "The Cat and The Hat Attack"  # Replace with the story title you want to query

#result = query_story_by_emotion_and_title(emotion, story_title)
#print(result)

#print(query_story_by_title("The Cat Attack"))

#print(query_stories_by_parts(8))