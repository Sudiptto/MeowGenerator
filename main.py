from flask import Flask, jsonify
from flask_cors import CORS
from errorBound import *
from prompt import *

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/meowGeneration/<storyTitle>/<catDescription>/<emotion>/<inspirationStory>/<parts>', methods=['GET'])
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

if __name__ == '__main__':
    app.run(debug=True)
