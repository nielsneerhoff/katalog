from __future__ import unicode_literals
import youtube_dl

from utils import BASE_DATA_DIRECTORY

download_options = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
        'preferredquality': '192',
    }],
    'nocheckcertificate': True,
    'outtmpl' : './{}/%(id)s.%(ext)s'.format(BASE_DATA_DIRECTORY)
}

def download_wav(video_url):
    with youtube_dl.YoutubeDL(download_options) as ydl:
        ydl.download([video_url])