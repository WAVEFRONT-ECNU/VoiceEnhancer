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
    save.output_file(savepath, filename, y, sr, '_org')
    return
