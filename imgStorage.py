# To store images on the cloud (we are using imgbb)
import requests
from passwords import *
import base64

def upload_image_to_imgbb(image_url, api_key):
    # Step 1: Download the image from the given URL
    try:
        response = requests.get(image_url)
        response.raise_for_status()
        image_data = response.content
    except requests.exceptions.RequestException as e:
        print(f"Error downloading the image: {e}")
        return None

    # Step 2: Convert the image data to a base64 encoded string
    encoded_image = base64.b64encode(image_data).decode('utf-8')

    # Step 3: Upload the image to ImgBB
    upload_url = "https://api.imgbb.com/1/upload"
    payload = {
        'key': api_key,
        'image': encoded_image,
    }

    try:
        upload_response = requests.post(upload_url, data=payload)
        upload_response.raise_for_status()
        result = upload_response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error uploading the image to ImgBB: {e}")
        return None

    # Step 4: Return the new URL of the uploaded image
    if result['status'] == 200:
        return result['data']['url']
    else:
        print(f"Error: {result['error']['message']}")
        return None

# Example usage
api_key = imgBBAPIKey  # Replace with your ImgBB API key
#image_url = 'https://placehold.co/600x400/png'
#new_image_url = upload_image_to_imgbb(image_url, api_key)
#print(f"New Image URL: {new_image_url}")
