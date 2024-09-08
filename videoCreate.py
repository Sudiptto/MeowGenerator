# Function to turn image to videos
import requests

# images is a list of image URLs
def generateVideo(images):
    # turn images into a string seperated by commas
    images = ",".join(images)

    base_url = 'http://127.0.0.1:8080/ImageToVideo/'

    # create request body
    response = requests.get(base_url + images)
    videoUrl = response.json()

    return videoUrl['video_url']


# WORKS
#print(generateVideo(["https://placehold.co/600x400/png", "https://placehold.co/600x500/png", "https://placehold.co/600x300/png/"]))