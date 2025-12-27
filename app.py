from flask import Flask, render_template, request
import google.generativeai as genai

genai.configure(api_key="____PASTE__YOUR__API__KEY____")
model = genai.GenerativeModel(model_name="models/gemma-3-27b-it")

app = Flask(__name__)
app.secret_key = "Yamini"

@app.route("/", methods = ["GET"])
def home():
    return render_template("index.html")

@app.route("/submit", methods = ["POST"])
def submit():
    if request.method == "POST":
        character = request.form["char"]
        sett = request.form["selection"]
        genre = request.form["genre"]
        age = request.form["age"]
        prompt = f"""
        Write a story with the following conditions:    
        - Main Character: {character}  
        - Story Type: {sett}  
        - Theme: {genre}   
        - Target Age Group: {age}  

        Make sure the story matches the theme, keeps the character central, and is written in a style appropriate for the given age group.
        Start typing story instantly, don't give any abbreviation.

        Make sure the story isn't to big, Make it a bit concise under 300-400 words.

        """
        response = model.generate_content(prompt)
        storyy = response.text
        
    return render_template("story.html", story = storyy)

if __name__ == "__main__":
    app.run(debug=True)
