import pandas as pd
from torchvision import datasets, transforms
from torch.utils.data import Dataset
import torchaudio

from release import get_release
import utils
from audio import download_wav

class AudioDataSet(Dataset):
    
    def __init__(self, csv_file):
        csv_data = pd.read_csv(csv_file)
        self.filenames = []
        self.labels = []
        for i in range(0, len(csv_data)):
            # Retrieve Youtube video url of Discogs release.
            discogs_id = csv_data.iloc[i, 0]
            release = get_release(discogs_id)
            video_url = release.videos[0].url
            # Download the .wav of the video, store it.
            download_wav(video_url)
            filename = utils.video_url_to_wav_filename(video_url)
            # Add to this data set.
            self.filenames.append(filename)
            self.labels.append(release.genres[0])

    def __getitem__(self, index):
        filename = self.filenames[index]
        tensor = ta.load(filename, normalization = True)
         # Downsample the audio to ~8kHz
        sound_data = self.mixer(tensor[0])

        # Account for audio clips that are too short
        temp_data = torch.zeros([160000, 1])
        if sound_data.numel() < 160000:
            tempData[:soundData.numel()] = sound_data[:]
        else:
            tempData[:] = sound_data[:160000]
        soundData = temp_data

        # Take every fifth sample of sound_data.
        sound_formatted = torch.zeros([32000, 1])
        sound_formatted[:32000] = sound_data[::5] 
        sound_formatted = sound_formatted.permute(1, 0)
        return sound_formatted, self.labels[index]

    def __len__(self):
        return len(self.file_names)


audio_data_set = AudioDataSet('test.csv')
print(4)