import VoiceEnhancer.enhance_speach


def denoise(inputfile: str):
    enhance_speach.enhance_speech(inputfile=inputfile)
    return
