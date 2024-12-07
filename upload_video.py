from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow

def get_authenticated_service():
    flow = InstalledAppFlow.from_client_secrets_file(
        'client_secrets.json',
        scopes=['https://www.googleapis.com/auth/youtube.upload']
    )
    credentials = flow.run_local_server(port=0)
    return build('youtube', 'v3', credentials=credentials)

def upload_video():
    youtube = get_authenticated_service()
    body = {
        'snippet': {
            'title': 'Test Video',
            'description': 'This is a test upload.',
            'tags': ['test', 'upload'],
            'categoryId': '22',  # People & Blogs
        },
        'status': {
            'privacyStatus': 'public',  # Set to "public" for visibility
        }
    }

    media = MediaFileUpload('test.mp4', chunksize=-1, resumable=True)
    request = youtube.videos().insert(part='snippet,status', body=body, media_body=media)

    response = request.execute()
    print("Upload response:", response)

if __name__ == "__main__":
    upload_video()
