# MeowGenerator API

## Table of Contents
- [Introduction](#introduction)
- [API Endpoints](#api-endpoints)
  - [Generate a Story Prompt](#generate-a-story-prompt)
  - [Get All Data](#get-all-data)
  - [Get Data by Emotion](#get-data-by-emotion)
  - [Get Data by Story Title](#get-data-by-story-title)
  - [Get Data by Number of Parts](#get-data-by-number-of-parts)
  - [Get Data by Emotion and Story Title](#get-data-by-emotion-and-story-title)
- [Setting Up](#setting-up)
  - [Creating `passwords.py`](#creating-passwordspy)
  - [Installing Requirements](#installing-requirements)
  - [Running the Application](#running-the-application)

## Introduction
This project provides an API for generating and retrieving story prompts based on various parameters. The API is built using Flask and requires certain API keys to function.

## API Endpoints

### Generate a Story Prompt
**Endpoint:** `/meowGeneration/<storyTitle>/<catDescription>/<emotion>/<inspirationStory>/<parts>`  
**Method:** `POST`  
**Description:** Generates a story prompt based on the provided parameters.

**Parameters:**
- `storyTitle` (string): The title of the story.
- `catDescription` (string): Description of the cat character.
- `emotion` (string): The emotion to be conveyed in the story.
- `inspirationStory` (string): The inspiration story.
- `parts` (integer): Number of parts/scenes in the story (between 1 and 15).

**Response:**
- `200 OK`: Returns the generated story prompt.
- `400 Bad Request`: Returns an error message if any parameter is invalid.

**Example Request:**
```sh
curl -X POST "http://<your-server-address>:<port>/meowGeneration/TheCatAdventure/A brave cat/Happy/A day in the park/5"

Get All Data
Endpoint: /meowData/getAllData
Method: GET
Description: Retrieves all data from storyData.json.

Response:

200 OK: Returns all data in JSON format.
Example Request:

curl -X GET "http://<your-server-address>:<port>/meowData/getAllData"

### get-all-data
Endpoint: /meowData/getDataByEmotion/<emotion>
Method: GET
Description: Retrieves data filtered by emotion.

Parameters:

emotion (string): The emotion to filter by.
Response:

200 OK: Returns data filtered by emotion in JSON format.
404 Not Found: Returns an error message if no data is found for the given emotion.
Example Request:

curl -X GET "http://<your-server-address>:<port>/meowData/getDataByEmotion/Happy"

### get-data-by-emotion
Endpoint: /meowData/getDataByTitle/<storyTitle>
Method: GET
Description: Retrieves data filtered by story title.

Parameters:

storyTitle (string): The title of the story to filter by.
Response:

200 OK: Returns data filtered by story title in JSON format.
404 Not Found: Returns an error message if no data is found for the given story title.
Example Request:

curl -X GET "http://<your-server-address>:<port>/meowData/getDataByTitle/TheCatAdventure"

Get Data by Number of Parts
Endpoint: /meowData/getDataByParts/<parts>
Method: GET
Description: Retrieves data filtered by the number of parts.

Parameters:

parts (integer): The number of parts to filter by.
Response:

200 OK: Returns data filtered by the number of parts in JSON format.
404 Not Found: Returns an error message if no data is found for the given number of parts.
Example Request:

curl -X GET "http://<your-server-address>:<port>/meowData/getDataByParts/5"

Get Data by Emotion and Story Title
Endpoint: /meowData/getDataByEmotionAndTitle/<emotion>/<storyTitle>
Method: GET
Description: Retrieves data filtered by both emotion and story title.

Parameters:

emotion (string): The emotion to filter by.
storyTitle (string): The title of the story to filter by.
Response:

200 OK: Returns data filtered by emotion and story title in JSON format.
404 Not Found: Returns an error message if no data is found for the given emotion and story title.
Example Request:

curl -X GET "http://<your-server-address>:<port>/meowData/getDataByEmotionAndTitle/Happy/TheCatAdventure"

Setting Up
Creating passwords.py
Create a file named passwords.py in the root directory of your project. This file will store your API keys securely.

# passwords.py

# OpenAI API Key
OPENAI_API_KEY = "your_openai_api_key_here"

# Any other API keys can be added here
# Example:
# OTHER_API_KEY = "your_other_api_key_here"

Make sure to add passwords.py to your .gitignore file to prevent it from being tracked by version control.

# .gitignore

passwords.py

Installing Requirements
To install the required dependencies listed in requirements.txt, run the following command:

pip install -r requirements.txt

Running the Application
To run the Flask application, execute the following command in your terminal:

python main.py

This will start the Flask server, and you can access the API endpoints as documented above.

By following this documentation, you should be able to set up and use the API, securely store your API keys, and install the necessary dependencies for your project.