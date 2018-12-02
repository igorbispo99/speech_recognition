#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
import numpy as np
import glob

from scipy.io import wavfile
from scipy.signal import spectrogram

AUDIO_FOLDERS = [
    'backward', 'bed', 'bird', 'cat', 'dog', 'down',
    'eight', 'five', 'follow', 'forward', 'four', 'go',
    'happy', 'house', 'learn', 'left', 'marvin', 'nine',
    'no', 'off', 'on', 'one', 'right', 'seven', 'sheila',
    'six', 'stop', 'three', 'two', 'up', 'visual', 'wow',
    'yes', 'zero', 'noise'
]

def generate_spec(filename):
    sr, data = wavfile.read(filename)
    fig,ax = plt.subplots(1)
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
    ax.axis('off')
    pxx, freqs, bins, im = ax.specgram(x=data, Fs=sr, noverlap=384, NFFT=512, cmap='gray')
    ax.axis('off')
    fig.canvas.draw()
    X = np.array(fig.canvas.renderer._renderer)[..., 0]
    plt.close()

    return X.reshape(X.shape[0], X.shape[1], 1)

def generate_all():
    for folder in AUDIO_FOLDERS:
        print("\nCurrently generating spectrograms for ", folder)
        curr_spect = []
        i = 0
        for f in glob.glob(folder + "/*.wav"):
            print("\r{}".format(i), end="")
            curr_spect.append(generate_spec(f))
            i += 1
        curr_spect = np.array(curr_spect)
        np.save("specs_vectors/" + folder + ".npy", curr_spect)
 


if __name__ == '__main__':
    generate_all()

