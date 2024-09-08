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

def checkInteger(intValue):
    try:
        intValue = int(intValue)
    except ValueError:
        return False
    return True

def checkInteger(value):
    try:
        # Try to convert the value to an integer
        intValue = int(value)
        # Check if converting back to float changes the value
        if float(value) != intValue:
            return False
        return True
    except ValueError:
        # If a ValueError is raised, the value is not an integer
        return False

def verifyParts(parts):
    # Try to convert parts to an integer
    
    if checkInteger(parts) == False:
        return False
    parts = int(parts)
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
