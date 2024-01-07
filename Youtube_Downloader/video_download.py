import pytube
import os
from pytube import YouTube

def video_download(url):
    yt = YouTube(url)
    video = yt.streams.first()
    out_file = video.download(output_path="../Youtube_Downloader/video")
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp4'
    os.rename(out_file, new_file)
    return new_file

if __name__ == "__main__":
    url = input("Enter the Youtube URL: ")
    video_download(url)
    print("Video Downloaded Successfully")