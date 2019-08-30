import requests
from bs4 import BeautifulSoup
from pytube import YouTube
count = 0
r = requests.get("https://www.youtube.com/playlist?list=PLxxA5z-8B2xk4szCgFmgonNcCboyNneMD")
c = r.content
soup = BeautifulSoup(c,"html.parser")
videolist = []
for link in soup.find_all('a'):
   tmp = 'https://www.youtube.com/playlist?list=PLxxA5z-8B2xk4szCgFmgonNcCboyNneMD'
   videolist.append(tmp)
count = 0
for item in videolist:
    count = count+1
    yt = YouTube(item)

    # have a look at the different formats available:
    # formats = yt.get_videos()
	

    # grab the video:
    video = yt.get('mp4', '360p')

    # set the output file name:
    #yt.set_filename('Video_' + str(count))

    # download the video:
    video.download('./')


