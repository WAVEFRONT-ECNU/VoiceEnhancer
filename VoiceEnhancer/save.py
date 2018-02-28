import wave
import numpy as np


def save_org(inputfile: str, params, winGain, xfinal):
    # 保存文件
    outputfile = inputfile
    wf = wave.open(outputfile, 'wb')
    # 设置参数
    wf.setparams(params)
    # 设置波形文件 .tostring()将array转换为data
    wave_data = (winGain * xfinal).astype(np.short)
    wf.writeframes(wave_data.tostring())
    wf.close()
    return


def save_enhanced(inputfile: str, params, winGain, xfinal):
    # 保存文件
    outputfile = inputfile[:-4] + "_enhanced.wav"
    wf = wave.open(outputfile, 'wb')
    # 设置参数
    wf.setparams(params)
    # 设置波形文件 .tostring()将array转换为data
    wave_data = (winGain * xfinal).astype(np.short)
    wf.writeframes(wave_data.tostring())
    wf.close()
    return
