from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq


app=Flask(__name__,
template_folder='templates',static_folder='static')



# Load environment variables
load_dotenv()
GROQ_API_KEY= os.getenv('GROQ_API_KEY')

# Defining LLM
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

def generate_bio(career, personality, interests, goals):
    # Create a prompt to feed into the ChatGroq model for bio generation
    prompt = (
        f"Create a unique and engaging bio with a suitable catchy title based on the following attributes:\n\n"
        f"Career: {career}\n"
        f"Personality: {personality}\n"
        f"Interests: {interests}\n"
        f"Relationship Goals: {goals}\n\n"
        f"Please generate a catchy title (like 'The Adventurous Foodie') followed by a bio in the following format:\n\n"
        f"**[Title]**\n\n"
        f"\"[Bio]\"\n\n"
        f"Examples of bio formats:\n"
        f"- The Adventurous Foodie\n"
        f"  \"Globe-trotting architect with a passion for spicy food and sustainable design. Seeking a fellow adventurer who can appreciate a good biryani and a thought-provoking conversation.\"\n\n"
        f"- The Creative Bookworm\n"
        f"  \"Introverted writer with a love for classic literature and indie coffee shops. Looking for someone who can match my wit and charm over a cup of chai and a deep discussion about our favorite novels.\"\n\n"
        f"Now, create a similar title and bio based on the given inputs."
    )
    
    messages = [
        ("system", "You are a helpful assistant who creates a bio along with a catchy title based on the given data, following the example format."),
        ("human", prompt),
    ]
    
    # Assuming 'llm.invoke' generates the response from the model
    ai_msg = llm.invoke(messages)
    
    # Output from the model should contain both title and bio
    print(f"LLM Response: {ai_msg.content}")
    
    # Assuming the response contains both the title and the bio, you can parse them
    # If it's in a format like "Title: <title>\nBio: <bio>", split accordingly:
    if ai_msg.content:
        # Split the response based on the title and the bio, assuming 'Title' and 'Bio' labels
        parts = ai_msg.content.split("\n", 1)
        if len(parts) > 1:
            title = parts[0].strip().lstrip("**").rstrip("**")
            bio = parts[1].strip()
            return title, bio
        else:
            return "No title and bio generated", ai_msg.content

    return "Error", "Failed to generate bio and title."





@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate_bio", methods=["POST"])
def generate():
    data = request.json
    career = data.get("career")
    personality = data.get("personality")
    interests = data.get("interests")
    goals = data.get("goals")

    title,bio = generate_bio(career, personality, interests, goals)
    return jsonify({"title": title, "bio": bio})







if __name__=="__main__":
    app.run(debug=False)
