from pytube import YouTube
from pytube import Playlist
import os
from sys import argv

#Gives download progress
def on_progress(stream, chunk, bytes_remaining):
    progress = f"{round(100 - (bytes_remaining/stream.filesize * 100),2)}%"
    print(f"progress: {progress}")

#Do this on download completion
def on_complete(stream, file_path):
    print("Download Completed")
    print(f"Download path: {file_path}")


#get playlist url from user
link = argv[1]

#Create Playlist obj
pl = Playlist(link) 

#Num of videos in playlist
video_count = pl.length
remaining_video_count = 0

print(f"Number of videos in the playlist: {video_count}")
print("Downloading started...")

#for every video in the playlist
for vids in pl.videos:
    vid_url = vids.watch_url
    yt = YouTube(url = vid_url, on_progress_callback=on_progress, on_complete_callback=on_complete)
    yd = yt.streams.filter(only_audio=True).first()
    out_file = yd.download('C:/Users/dijk/Music/youtube-pyth-downloads')
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    remaining_video_count +=1
    print("\n")

