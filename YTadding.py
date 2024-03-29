# -*- coding: utf-8 -*-

# Sample Python code for youtube.playlistItems.insert
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]


scopeSpreadSheet = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('TestSpreadsheet.json', scopeSpreadSheet)
client = gspread.authorize(creds)

sheet = client.open('Pysheets').sheet1



playlistId = "PLrCCqE1vWhlw2ucFzeUT0_wyk4TKmlJ_G"
videoId = "ljRAR8LXo1k"
def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "MY_CLIENT_SECRESTS.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    request = youtube.playlistItems().insert(
        part="snippet",
        body={
          "snippet": {
            "playlistId": playlistId,
            "position": 0,
            "resourceId": {
              "kind": "youtube#video",
              "videoId": videoId
            }
          }
        }
    )
    response = request.execute()

    print(response)

if __name__ == "__main__":
    main()
