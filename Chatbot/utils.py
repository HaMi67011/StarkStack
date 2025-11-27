import os
from dotenv import load_dotenv

load_dotenv()

def load_api_key():
    key = os.getenv('GROQ_API_KEY')
    if key:
        key = key.replace("\ufeff", "").strip().strip('"').strip("'")
        if key.startswith("gsk_"):
            print("Loaded API key from .env")
            return key
        else:
            print("Invalid Groq API key format in .env")
    # If not found in env, ask user
    while True:
        path = input("Enter path to your API key file: ").strip()
        path = path.strip('"').strip("'")
        if not os.path.isfile(path):
            print("File not found. Try again.\n")
            continue
        with open(path, "r", encoding="utf-8") as f:
            key = f.read()
        key = key.replace("\ufeff", "").strip().strip('"').strip("'")
        if key.startswith("gsk_"):
            return key
        print("ERROR: Invalid Groq API key format.\n")
