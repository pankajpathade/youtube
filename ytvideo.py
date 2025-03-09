from pytubefix import YouTube as Video

def main():
    url =input("Enter your url: ")
    download_video(url)

def download_video(url):
    video = Video(url)
    stream = video.streams.get_highest_resolution()
    stream.download()
    print(f"Title:{video.title}\nStatus:download successful")

if __name__== "__main__":
    main()