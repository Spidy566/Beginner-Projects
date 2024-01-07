import os

from pytube import YouTube

def url_to_mp3(url):
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download(output_path="../Youtube_Downloader/audio")
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    return new_file

if __name__ == "__main__":
    url = input("Enter the Youtube URL: ")
    url_to_mp3(url)
    print("Audio Downloaded Successfully")