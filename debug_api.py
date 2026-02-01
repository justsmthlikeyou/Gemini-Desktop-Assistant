import sys
import os
import traceback
from dotenv import load_dotenv
from google import genai

# Setup environment
base_dir = os.path.dirname(os.path.abspath(__file__))
dotenv_path = os.path.join(base_dir, '.env')
load_dotenv(dotenv_path)

api_key = os.getenv("GOOGLE_API_KEY")

print(f"--- Gemini API Diagnostic ---")
print(f"CWD: {os.getcwd()}")
print(f".env path: {dotenv_path}")
print(f"API Key present: {'Yes' if api_key else 'NO'}")

if not api_key:
    print("CRITICAL: No API Key found.")
    sys.exit(1)

client = genai.Client(api_key=api_key)

models_to_test = ["gemini-2.5-flash", "gemini-2.0-flash"]

for model in models_to_test:
    print(f"\nTesting model: {model}...")
    try:
        response = client.models.generate_content(
            model=model,
            contents="Hello, are you working?"
        )
        print(f"SUCCESS! Response: {response.text}")
        break # Stop if one works
    except Exception as e:
        print(f"FAILED.")
        print(f"Error Type: {type(e).__name__}")
        print(f"Error Message: {str(e)}")
        # print(traceback.format_exc()) # Uncomment for full stack trace

print("\n--- Diagnostic Finished ---")
print("If you see 404 Not Found, checking model availability.")
print("If you see 403 Permission Denied, check your API Key.")
print("If you see 429 Resource Exhausted, you are rate limited.")
