from pytube import YouTube
from sys import argv

link = argv[1]
yt = Playlist(link)

print("Title: ", yt.title)
print("View: ", yt.views)

yd = yt.streams.get_highest_resolution()
yd.download('C:/Users/dijk/Videos/youtube-py-downloads')

print("Download Successful: ", yt.title)
 
