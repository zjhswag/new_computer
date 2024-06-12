from pydub import AudioSegment

# 加载OGG文件，注意使用原始字符串或双反斜杠避免转义字符问题
sound = AudioSegment.from_ogg(r"C:\Users\14601\Music\en - 你不知道的事.ogg")

# 导出为WAV
sound.export(r"C:\Users\14601\Music\a.wav", format="wav")
