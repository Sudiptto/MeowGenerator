from flask import Flask, jsonify
from flask_cors import CORS
from errorBound import *

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/meowGeneration/<storyTitle>/<catDescription>/<emotion>/<inspirationStory>/<parts>', methods=['POST'])
def meowGeneration(storyTitle, catDescription, emotion, inspirationStory, parts):

    # Develop error bounds to check if parts is an integer, and storyTitle - inspirationStory are strings that are appropriate lengths 

    
    return f"All Data: {storyTitle}, {catDescription}, {emotion}, {inspirationStory}, {parts}"

if __name__ == '__main__':
    app.run(debug=True)
