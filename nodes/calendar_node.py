import pickle
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

class CalendarNode:
    """
    Node to process calendar actions with error handling
    """
    SCOPES = ["https://www.googleapis.com/auth/calendar"]

    def __init__(self, token_file="token.json"):
        self.token_file = token_file
        self.creds = None
        self.service = None
        self._load_credentials()

    def _load_credentials(self):
        try:
            with open(self.token_file, "rb") as token:
                self.creds = pickle.load(token)
            self.service = build("calendar", "v3", credentials=self.creds)
        except FileNotFoundError:
            print(f"Error: {self.token_file} not found. Run the OAuth flow to create it.")
        except Exception as e:
            print("Failed to load credentials:", e)

    def process(self, intent_data):
        if not self.service:
            return "Calendar service not available. Check credentials."

        action = intent_data.get("action")
        if action == "add_event":
            event = {
                "summary": intent_data["title"],
                "start": {"dateTime": intent_data["datetime"], "timeZone": "America/New_York"},
                "end": {"dateTime": intent_data["datetime"], "timeZone": "America/New_York"},
            }
            try:
                self.service.events().insert(calendarId="primary", body=event).execute()
                return f"Event '{intent_data['title']}' added!"
            except Exception as e:
                return f"Failed to add event: {e}"

        elif action == "list_events":
            try:
                events = self.service.events().list(
                    calendarId="primary", maxResults=5, singleEvents=True, orderBy="startTime"
                ).execute()
                event_list = [e["summary"] for e in events.get("items", [])]
                if not event_list:
                    return "No upcoming events."
                return f"Upcoming events: {', '.join(event_list)}"
            except Exception as e:
                return f"Failed to fetch events: {e}"

        return "Action not supported."
