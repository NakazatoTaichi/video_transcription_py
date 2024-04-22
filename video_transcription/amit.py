import ffmpeg
import speech_recognition as sr

stream = ffmpeg.input("ファイルのパスを取得")

stream = ffmpeg.output(stream, "wav/命名.wav")

ffmpeg.run(stream)

r = sr.Recognizer()
with sr.AudioFile("wav/命名.wav") as source:
    audio = r.record(source)
text = r.recognize_google(audio, language='ja-JP')
print(text)