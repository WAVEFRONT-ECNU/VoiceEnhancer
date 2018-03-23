import librosa

'''------------------------------------
FILE READER:
    receives filename,
    returns audio time series (y) and sampling rate of y (sr)
------------------------------------'''


def read_file(file_name, sample_directory=""):
    sample_file = file_name
    # sample_directory = ''
    sample_path = sample_directory + sample_file

    # generating audio time series and a sampling rate (int)
    y, sr = librosa.load(sample_path)

    return y, sr
