from flask import Flask, jsonify
from flask_cors import CORS
from errorBound import *
from prompt import *
from parseData import *

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# main API route for generating a story prompt
@app.route('/meowGeneration/<storyTitle>/<catDescription>/<emotion>/<inspirationStory>/<parts>', methods=['POST'])
def meowGeneration(storyTitle, catDescription, emotion, inspirationStory, parts):
    
    if verifyStoryTitle(storyTitle) == False:
        return jsonify({"error": "Invalid story title"})
    
    if verifyCatDescription(catDescription) == False:
        return jsonify({"error": "Make sure the description is between 50 and 400 words"})
    
    if verifyEmotion(emotion) == False:
        return jsonify({"error": "Invalid emotion"})
    
    if verifyInspirationStory(inspirationStory) == False:
        return jsonify({"error": "Make sure the inspiration story is between 50 and 500 words"})
    
    if verifyParts(parts) == False:
        print(type(parts))
        return jsonify({"error": "Make sure parts is a number between 1 and 15"})
    
    response = generate_story_prompt(storyTitle, catDescription, emotion, inspirationStory, parts)
    return response

# the below API all revolve around parsing the data from storyData.json

# route to get all data
@app.route("/meowData/getAllData", methods=['GET'])
def getAllData():
    return get_all_data()

# route to get data by emotion
@app.route("/meowData/getDataByEmotion/<emotion>", methods=['GET'])
def getDataByEmotion(emotion):
    return query_stories_by_emotion(emotion)

# route to get data by story title
@app.route("/meowData/getDataByTitle/<storyTitle>", methods=['GET'])
def getDataByTitle(storyTitle):
    return query_story_by_title(storyTitle)

# route to get data by number of parts
@app.route("/meowData/getDataByParts/<parts>", methods=['GET'])
def getDataByParts(parts):
    if checkInteger(parts) == False:
        return jsonify({"error": "Make sure parts is a number between 1 and 15"})
    
    # check if parts is an integer first
    return query_stories_by_parts(int(parts))

# route to get data by emotion and story title
@app.route("/meowData/getDataByEmotionAndTitle/<emotion>/<storyTitle>", methods=['GET'])
def getDataByEmotionAndTitle(emotion, storyTitle):
    return query_story_by_emotion_and_title(emotion, storyTitle)

# route to get data by number of parts

if __name__ == '__main__':
    app.run(debug=True)
