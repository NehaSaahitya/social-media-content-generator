import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
print("Loaded API Key:", api_key)  # Debug line

client = Groq(api_key=api_key)

def generate_social_media_content(topic, platform):
    prompt = f"""
    You are a professional Social Media Content Creator AI.

    Generate:
    - 5 content ideas about: "{topic}"
    - For each idea:
        * One catchy platform-specific caption
        * 5–8 relevant hashtags

    Platform chosen: {platform}
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are a social media content generator."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
