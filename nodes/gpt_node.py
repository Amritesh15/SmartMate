# nodes/gpt_node.py
import os
import json
from dotenv import load_dotenv
from openai import OpenAI
import openai  # for exceptions

# Load .env first
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class GPTNode:
    def process(self, message: str):
        prompt = f"""
        Extract intent from this message and return as JSON:
        Actions can be: add_event, list_events, delete_event, weather, notes
        Message: "{message}"
        """
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            output = response.choices[0].message.content
            try:
                return json.loads(output)
            except json.JSONDecodeError:
                print("GPTNode JSON parsing error, returning raw message")
                return {"action": "unknown", "raw": message, "error": "Invalid JSON from GPT"}
        except openai.error.RateLimitError:
            print("GPTNode rate limit reached")
            return {"action": "unknown", "raw": message, "error": "OpenAI quota exceeded"}
        except openai.OpenAIError as e:
            print(f"GPTNode API error: {e}")
            return {"action": "unknown", "raw": message, "error": str(e)}
        except Exception as e:
            print(f"GPTNode unexpected error: {e}")
            return {"action": "unknown", "raw": message, "error": str(e)}
