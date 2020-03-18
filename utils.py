BASE_DATA_DIRECTORY = './data/'

def video_url_to_wav_filename(video_url):
    video_id = parse_video_id(video_url)
    return BASE_DATA_DIRECTORY + video_id + '.wav'

def parse_video_id(video_url):
    start_index = video_url.index('=') + 1
    end_index = len(video_url)
    return video_url[start_index : end_index]