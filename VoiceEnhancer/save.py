import librosa
import os

'''------------------------------------
OUTPUT GENERATOR:
    receives a destination path, file name, audio matrix, and sample rate,
    generates a wav file based on input
------------------------------------'''


def output_file(destination, filename, y, sr, ext=""):
    '''------------------------------------
    if not os.path.exists(destination):
        os.mkdir(destination)
    ------------------------------------'''
    destination = destination + filename[:-4] + ext + '.wav'
    librosa.output.write_wav(destination, y, sr)
