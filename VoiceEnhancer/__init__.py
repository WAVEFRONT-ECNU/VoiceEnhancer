import VoiceEnhancer.enhance_speach
import VoiceEnhancer.save


def denoise(inputfile: str):
    params, winGain, xfinal = enhance_speach.enhance_speech(inputfile=inputfile)
    # 默认写入原文件。可选添加"_enhanced"后缀。
    save.save_org(inputfile=inputfile, params=params, winGain=winGain, xfinal=xfinal)
    # save.save_enhanced(inputfile=inputfile, params=params, winGain=winGain, xfinal=xfinal)
    return
