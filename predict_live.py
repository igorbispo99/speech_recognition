import sounddevice as sd
import numpy as np
import time
import os
import generate_spectrogram as gs
import matplotlib.pyplot as plt
import cv2 as cv

os.environ["KERAS_BACKEND"] = "plaidml.keras.backend"

from keras.models import load_model

sd.default.samplerate = 16000
sd.default.channels = 1
fs = 16000

def process_spec(s):
    spect = s
    spect = cv.resize(spect, (96 , 96)).reshape((96, 96, 1))
    spect = np.stack((spect, spect, spect), axis=2).reshape((1, 96, 96, 3))
    spect = spect * 1/255

    return spect

def gen_spect(data):
    sr = fs
    data = data.reshape(16000)

    fig,ax = plt.subplots(1)
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
    ax.axis('off')

    pxx, freqs, bins, im = ax.specgram(x=data, Fs=sr, noverlap=384, NFFT=512, cmap='gray')
    ax.axis('off')

    fig.canvas.draw()

    X = np.array(fig.canvas.renderer._renderer)[..., 0]
    plt.close()

    return X.reshape(X.shape[0], X.shape[1], 1)

def listen():
    model = load_model("cnn_audio.h5")
    name_window = "Spectrogram"

    while(1):
        r = sd.rec(int(fs))
        sd.wait()
        r_spect = gen_spect(r)
        processed_r = process_spec(r_spect)

        cv.imshow(name_window, r_spect.reshape((480, 640)))

        if cv.waitKey(1) & 0xFF == ord('q'):
            break

        p = model.predict(processed_r)
        label = gs.AUDIO_FOLDERS[p.argmax()]

        if p.max() > 0.9:
            print("Word labed as \"{0}\" with a confidence of {1:.3f}".format(label, p.max()))
            cv.imwrite("out.png", r_spect.reshape((480, 640)))

if __name__ == "__main__":
    print("")
    listen()





