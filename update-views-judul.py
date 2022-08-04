import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


#scopes
scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]


def main():
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    client_secrets_file = "secret1.json" #oAuth
    
     
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', scopes)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                client_secrets_file, scopes)
            creds = flow.run_console()
            
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())


        yt = build('youtube', 'v3', credentials=creds) 

        req = yt.videos().list(
            part="snippet,statistics",
            id="YqKVKQOYu6Y"
            )
        response = req.execute();
        data = response["items"][0];
        snippet = data["snippet"];
        title_sblm = snippet["title"];

        views = int(data["statistics"]["viewCount"]);
        title_baru = f"Video ini telah ditonton {views:,} kali. Kok bisa ?" #new title
        print(title_baru)
        if(title_sblm != title_baru):
            snippet["title"] = title_baru; 

        req = yt.videos().update(
                part="snippet",
                body={
                    "id": "YqKVKQOYu6Y",
                    "snippet": snippet
                }
        )
        response = req.execute();

main()
