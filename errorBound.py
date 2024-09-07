# Check the error bounds 

# storyTitle verification
# around 5 characters - 100 characters
def verifyStoryTitle(storyTitle):
    
    # if story title all empty than return False
    if storyTitle.isspace():
        return False

    # less than 10 characters, excluding spaces
    if len(storyTitle) < 5:
        return False
    # greater than 100
    if len(storyTitle) > 100:
        return False
    
    return True
