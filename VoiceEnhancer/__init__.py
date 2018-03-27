import VoiceEnhancer.noise_reduce
import VoiceEnhancer.read
import VoiceEnhancer.save

'''------------------------------------
LOGIC:
    [1] load file
    [2] reduce noise
    [3] trim silence
    [4] output file

------------------------------------'''


def noise_reduction(filename: str):
    # reading a file
    y, sr = read.read_file(filename)

    # reducing noise using db power
    y_reduced_power = noise_reduce.reduce_noise_power(y, sr)
    y_reduced_centroid_s = noise_reduce.reduce_noise_centroid_s(y, sr)
    y_reduced_centroid_mb = noise_reduce.reduce_noise_centroid_mb(y, sr)
    y_reduced_mfcc_up = noise_reduce.reduce_noise_mfcc_up(y, sr)
    y_reduced_mfcc_down = noise_reduce.reduce_noise_mfcc_down(y, sr)
    y_reduced_median = noise_reduce.reduce_noise_median(y, sr)

    # trimming silences
    y_reduced_power = noise_reduce.trim_silence(y_reduced_power)
    y_reduced_centroid_s = noise_reduce.trim_silence(y_reduced_centroid_s)
    y_reduced_centroid_mb = noise_reduce.trim_silence(y_reduced_centroid_mb)
    y_reduced_mfcc_up = noise_reduce.trim_silence(y_reduced_mfcc_up)
    y_reduced_mfcc_down = noise_reduce.trim_silence(y_reduced_mfcc_down)
    y_reduced_median = noise_reduce.trim_silence(y_reduced_median)

    # generating output file
    savepath = ""

    save.output_file(savepath, filename, y_reduced_power, sr, '_pwr')
    save.output_file(savepath, filename, y_reduced_centroid_s, sr, '_ctr_s')
    save.output_file(savepath, filename, y_reduced_centroid_mb, sr, '_ctr_mb')
    save.output_file(savepath, filename, y_reduced_mfcc_up, sr, '_mfcc_up')
    save.output_file(savepath, filename, y_reduced_mfcc_down, sr, '_mfcc_down')
    save.output_file(savepath, filename, y_reduced_median, sr, '_median')
    # save.output_file(savepath, filename, y, sr, '_org')
    return


def noise_reduction_all(filename: str):
    # reading a file
    y, sr = read.read_file(filename)
    y_reduced = y

    # reducing noise using db power
    y_reduced = noise_reduce.reduce_noise_power(y_reduced, sr)
    y_reduced = noise_reduce.reduce_noise_centroid_s(y_reduced, sr)
    y_reduced = noise_reduce.reduce_noise_centroid_mb(y_reduced, sr)
    y_reduced = noise_reduce.reduce_noise_mfcc_up(y_reduced, sr)
    y_reduced = noise_reduce.reduce_noise_mfcc_down(y_reduced, sr)
    y_reduced = noise_reduce.reduce_noise_median(y_reduced, sr)

    # trimming silences
    y_reduced = noise_reduce.trim_silence(y_reduced)

    # generating output file
    savepath = ""

    save.output_file(savepath, filename, y_reduced, sr, '_enhc')
    # save.output_file(savepath, filename, y, sr, '_org')
    return


def noise_reduction_single_mode(filename: str, mode: str):
    # reading a file
    y, sr = read.read_file(filename)
    y_reduced = y

    # reducing noise using db power
    if mode == "power":
        y_reduced = noise_reduce.reduce_noise_power(y_reduced, sr)
    elif mode == "centroid_s":
        y_reduced = noise_reduce.reduce_noise_centroid_s(y_reduced, sr)
    elif mode == "centroid_mb":
        y_reduced = noise_reduce.reduce_noise_centroid_mb(y_reduced, sr)
    elif mode == "mfcc_up":
        y_reduced = noise_reduce.reduce_noise_mfcc_up(y_reduced, sr)
    elif mode == "mfcc_down":
        y_reduced = noise_reduce.reduce_noise_mfcc_down(y_reduced, sr)
    elif mode == "median":
        y_reduced = noise_reduce.reduce_noise_median(y_reduced, sr)

    # trimming silences
    y_reduced = noise_reduce.trim_silence(y_reduced)

    # generating output file
    savepath = ""
    savename = "_" + mode

    save.output_file(savepath, filename, y_reduced, sr, savename)
    # save.output_file(savepath, filename, y, sr, '_org')
    return
