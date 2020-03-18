import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import Dataset
import torchaudio as ta
import pandas as pd
import numpy as np

import utils
import audio

class AudioDataSet(Dataset):

    def __init__(self, csv_file):
        csv_data = pd.read_csv(csv_file)
        self.file_names = []
        self.labels = []
        for i in range(0, len(csv_data)):
            
            self.file_names.append(csv_data)
            self.labels.append(csvData.iloc[i, 6])

        self.file_path = file_path
        self.mixer = ta.transforms.DownmixMono() #UrbanSound8K uses two channels, this will convert them to one
        self.folderList = folderList

    def __getitem__(self, index):
        #format the file path and load the file
        path = self.file_path + "fold" + str(self.folders[index]) + "/" + self.file_names[index]
        sound = torchaudio.load(path, out = None, normalization = True)
        #load returns a tensor with the sound data and the sampling frequency (44.1kHz for UrbanSound8K)
        soundData = self.mixer(sound[0])
        #downsample the audio to ~8kHz
        tempData = torch.zeros([160000, 1]) #tempData accounts for audio clips that are too short
        if soundData.numel() < 160000:
            tempData[:soundData.numel()] = soundData[:]
        else:
            tempData[:] = soundData[:160000]
        
        soundData = tempData
        soundFormatted = torch.zeros([32000, 1])
        soundFormatted[:32000] = soundData[::5] #take every fifth sample of soundData
        soundFormatted = soundFormatted.permute(1, 0)
        return soundFormatted, self.labels[index]
    
    def __len__(self):
        return len(self.file_names)

def load_tensor(wav_filename):
    return ta.load(wav_filename)

def save_tensor(tensor, tensor_filename, waveform, sample_rate):
    return ta.save(tensor_filename, waveform, sample_rate)