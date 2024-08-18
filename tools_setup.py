import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

# Configure the Gemini model
gemini_model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.7)

# If you have other tools to configure, do so here. For now, just return the Gemini model
def get_language_model():
    return gemini_model
