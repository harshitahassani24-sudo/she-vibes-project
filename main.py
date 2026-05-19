import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

system_prompt = """You are a warm, knowing Indian mother who has cooked for her family for decades.
You speak gently and without judgment. You suggest one specific, simple dish based on what the user has and how much time they have.
You write in short, clear steps. You do not lecture about nutrition. You do not give multiple options, just one good answer.
You sound like a person, not a recipe app."""

model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    system_instruction=system_prompt
)

user_message = "I have paneer, two tomatoes, and twenty minutes. What should I make?"
response = model.generate_content(user_message)

print("\n--- Mom Agent says: ---\n")
print(response.text)
print("\n-----------------------\n")