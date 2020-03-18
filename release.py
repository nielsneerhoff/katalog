import os

import audio
import net
import utils

from dotenv import load_dotenv
from discogs_client import Client

load_dotenv()
DISCOGS_USER_TOKEN = os.getenv('DISCOGS_USER_TOKEN')
discogs_api = Client('Katalog', user_token = DISCOGS_USER_TOKEN)

def get_release(discogs_id):
    return discogs_api.release(discogs_id)

# release = get_release(34534)
# video_urls = [video.url for video in release.videos]
# styles = release.styles
# genres = release.genres

# audio.download_wav(video_urls[0])
# wav_filename = utils.video_url_to_wav_filename(video_urls[0])
# import IPython.display as play
# play.Audio(wav_filename)
# waveform, samplerate = net.load_tensor(wav_filename)
# print(40)