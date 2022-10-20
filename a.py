from pytube import YouTube

print("Empezando")
link = "https://www.youtube.com/watch?v=2Vv-BfVoq4g"
yt = YouTube(link)

for pistas in yt.streams:
    print(pistas)

mp3 = yt.streams.get_audio_only()
print("Descargando")
mp3.download()


