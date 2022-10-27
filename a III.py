from pytube import YouTube
from pytube import Playlist



    
def descargarplaylist(url:str):
   
    playlist=Playlist(url)
    for cancion in playlist.videos:
        print("Descargando cancion: ")
        cancion.stream.get_audio_only().download("Canciones/")
url="https://www.youtube.com/playlist?list=PLAcee9FMaCc54OG0OjuZReqv4gFvIfRa4"
descargarplaylist (url)