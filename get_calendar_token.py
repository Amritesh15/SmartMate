from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import pickle

SCOPES = ['https://www.googleapis.com/auth/calendar']

def main():
    flow = InstalledAppFlow.from_client_secrets_file(
        'credentials.json', SCOPES)
    creds = flow.run_local_server(port=0)

    # Save the credentials for later use
    with open('token.json', 'wb') as token:
        pickle.dump(creds, token)
    print("token.json created!")

if __name__ == '__main__':
    main()
