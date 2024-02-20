# importing packages
from pytube import YouTube
from sys import argv
import os

link = argv[1]
yt = YouTube(link)

# extract only audio
video = yt.streams.filter(only_audio=True).first()

# download the file
out_file = video.download('C:/Users/dijk/Music/youtube-pyth-downloads')

# save the file
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)

# result of success
print("Download Successfull: ", yt.title)
