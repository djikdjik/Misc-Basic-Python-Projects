#first run -> pip install pytube
from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print("Title: ", yt.title)
print("View: ", yt.views)

yd = yt.streams.get_highest_resolution()
file_size = round((yd.filesize / 1000000), 2)
print(f"File Size: {file_size} MB")
yd.download('C:/Users/dijk/Videos/youtube-py-downloads')

print("Download Successful: ", yt.title)

