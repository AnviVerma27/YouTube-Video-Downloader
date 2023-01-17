from pytube import YouTube

yt = YouTube(input("enter the link"))

print("Title: ",yt.title)
print("View: ",yt.views)

yd = yt.streams.get_highest_resolution()

path = input("enter the path for saving the downloaded file")
yd.download(path)
# yd.download('/Users/acer/Dropbox/PC/Downloads')
