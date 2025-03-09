from pytubefix import Playlist

def main():
    url = input("Enter your URL:")
    download_playlist(url)


def download_playlist(url):
    pl = Playlist(url)
    for video in pl.videos:
        stream =video.streams.get_highest_resolution()
        stream.download()
        print(f"Title:{video.title}\nStatus:download successful")


if __name__ == "__main__":
    main()