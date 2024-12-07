# YouTube Video Uploader
## This project is a Python script for uploading videos to YouTube using the YouTube Data API v3. It allows users to programmatically upload videos by providing necessary details like the title, description, tags, and privacy settings.

## Requirements
### Libraries
#### The following Python libraries are required:

    google-auth
    google-auth-oauthlib
    google-auth-httplib2
    google-api-python-client

#### To install these libraries, enter the following command in the terminal:
    pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client

## 1. Setup
#### • Go to the Google Cloud Console
#### • Create a new project or use an existing one.
#### • Enable the YouTube Data API v3 for your project.
#### • Create OAuth 2.0 credentials and download the client_secrets.json file.
#### • Place the client_secrets.json file in the same directory as the script.

## Configure Your Script:

#### • Replace the video details (e.g., title, description, and tags) with your own.

## How to use

#### Run the script by typing the following command in the terminal:
    python uploader.py

## Authenticate

#### • A browser window will open, prompting you to log in and grant access to your YouTube account.
#### • Copy and paste the authentication code into the terminal if required.

## Upload your video
#### • The script will upload your specified video to your YouTube Channel.


