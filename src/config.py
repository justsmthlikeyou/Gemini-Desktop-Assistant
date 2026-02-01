import os
import sys
from dotenv import load_dotenv

# Load .env file
# Explicitly find the .env file in the project root (parent of 'src')
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dotenv_path = os.path.join(base_dir, '.env')
load_dotenv(dotenv_path)

# Debugging
print(f"DEBUG: CWD: {os.getcwd()}")
print(f"DEBUG: Config file: {__file__}")
print(f"DEBUG: Calculated .env path: {dotenv_path}")

if os.path.exists(dotenv_path):
    size = os.path.getsize(dotenv_path)
    print(f"DEBUG: .env file FOUND. Size: {size} bytes")
    if size == 0:
        print("DEBUG: WARNING: .env file is EMPTY!")
else:
    print(f"DEBUG: .env file NOT FOUND at: {dotenv_path}")

load_dotenv(dotenv_path)

def get_api_key():
    """Retrieves the Google API Key from environment variables."""
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("Error: GOOGLE_API_KEY not found in .env file.")
        print("Please create a .env file based on .env.example and add your API Key.")
        sys.exit(1)
    return api_key

def get_hotkey():
    """Retrieves the hotkey from environment variables or returns default."""
    return os.getenv("HOTKEY", "<alt>+x")
