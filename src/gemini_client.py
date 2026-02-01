from google import genai
from .config import get_api_key

class GeminiClient:
    def __init__(self):
        self.api_key = get_api_key()
        self.client = genai.Client(api_key=self.api_key)

    def get_response(self, text: str) -> str:
        """Sends text to Gemini and returns the response."""
        try:
            # Using the latest SDK pattern
            response = self.client.models.generate_content(
                model="gemini-2.5-flash",
                contents=text
            )
            return response.text
        except Exception as e:
            error_msg = str(e)
            if "429" in error_msg or "Resource has been exhausted" in error_msg:
                return "⚠️ Rate Limit Exceeded.\n\nYou are using the Free Tier, which has usage limits. Please wait a minute before trying again."
            
            return f"Error communicating with Gemini:\n{error_msg}"
