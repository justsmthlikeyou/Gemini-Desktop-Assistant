import os
from dotenv import load_dotenv
from google import genai

# Load env safely
base_dir = os.path.dirname(os.path.abspath(__file__))
dotenv_path = os.path.join(base_dir, '.env')
load_dotenv(dotenv_path)

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    print("No API Key found.")
    exit(1)

client = genai.Client(api_key=api_key)

print("Fetching available models...")
try:
    # List models that support generateContent
    pager = client.models.list()
    print(f"{'Model Name':<30} | {'DisplayName':<30}")
    print("-" * 65)
    
    count = 0
    for model in pager:
        # Debugging: Print structure of the first model to understand the SDK
        if count == 0:
            print("DEBUG: First Model Object Attributes:")
            print(dir(model))
            print("-" * 30)
        
        # Try to access common attributes safely
        try:
            # Inspect known possible attributes
            name = getattr(model, "name", "N/A")
            display = getattr(model, "display_name", "N/A")
            print(f"Found Model: {name} (Display: {display})")
            
            # Print full object for clarity
            # print(model) 
            count += 1
        except Exception:
            pass

    if count == 0:
        print("No models found.")
        
except Exception as e:
    print(f"Error listing models: {e}")
