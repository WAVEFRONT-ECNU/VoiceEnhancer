import VoiceEnhancer.enhance_speach
import VoiceEnhancer.save


def denoise(inputfile: str):
    params, winGain, xfinal = enhance_speach.enhance_speech(inputfile=inputfile)
    # Write to original file default. XXX_enhanced.wav Alternative.
    save.save_org(inputfile=inputfile, params=params, winGain=winGain, xfinal=xfinal)
    # save.save_enhanced(inputfile=inputfile, params=params, winGain=winGain, xfinal=xfinal)
    return
