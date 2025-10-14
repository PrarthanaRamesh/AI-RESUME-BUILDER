import os
import google.generativeai as genai
from dotenv import load_dotenv

print("Attempting to check available models...")

try:
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")

    if api_key:
        print("API Key found in .env file.")
        genai.configure(api_key=api_key)

        print("\n--- Available Models ---")
        for m in genai.list_models():
            # We only care about models that support content generation
            if 'generateContent' in m.supported_generation_methods:
                print(m.name)
        print("------------------------\n")
        print("Diagnostic complete. If you see model names above, copy the list and share it.")

    else:
        print("ERROR: Google API Key not found in .env file. Please check your .env file.")

except Exception as e:
    print(f"An error occurred: {e}")