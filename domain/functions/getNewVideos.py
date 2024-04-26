from googleapiclient.discovery import build
from data.util.tokens import *

youtube = build('youtube', 'v3', developerKey=GOOGLE_API_KEY)


def get_latest_video():
    request = youtube.search().list(
        part='snippet',
        channelId=CHANNEL_ID,
        order='date',
        maxResults=1
    )
    response = request.execute()
    latest_video_info = response['items'][0]

    return latest_video_info

def getLatestVideo():
    latest_video_info = get_latest_video()
    videoLink = f"https://www.youtube.com/shorts/{latest_video_info['id']['videoId']}"
    return videoLink
