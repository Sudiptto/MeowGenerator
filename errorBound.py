import re

def verifyStoryTitle(storyTitle):
    # if story title is all empty then return False
    if storyTitle.isspace():
        return False
    
    # less than 5 characters or more than 100 characters
    if len(storyTitle) < 5 or len(storyTitle) > 100:
        return False
    
    return True

def verifyCatDescription(catDescription):
    # Check if description is empty
    if catDescription.isspace():
        return False
    
    # Check for word count
    word_count = len(catDescription.split())
    if word_count < 50 or word_count > 400:
        return False
    
    return True

def verifyEmotion(emotion):
    # Check if emotion is empty
    if emotion.isspace():
        return False
    
    # Check length of emotion string
    if len(emotion) < 3 or len(emotion) > 50:
        return False
    
    return True

def verifyInspirationStory(inspirationStory):
    # Check if inspiration story is empty
    if inspirationStory.isspace():
        return False
    
    # Check for word count
    word_count = len(inspirationStory.split())
    if word_count < 50 or word_count > 500:
        return False
    
    return True

def verifyParts(parts):
    # Try to convert parts to an integer
    try:
        parts = int(parts)
    except ValueError:
        return False
    
    # Check if parts is between 1 and 15
    if parts < 1 or parts > 15:
        return False
    
    return True


# Example usage
"""print(verifyStoryTitle("A brief story"))  # True
print(verifyCatDescription("This is a description that has more than 200 words..."))  # Depends on the content
print(verifyEmotion("Happy"))  # Depends on length
print(verifyInspirationStory("This is an inspirational story that contains more than 200 words..."))  # Depends on the content
print(verifyParts(5))  # True"""

