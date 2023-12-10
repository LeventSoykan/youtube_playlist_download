from pytube import Playlist
import pytube
import re
from concurrent.futures import ThreadPoolExecutor, as_completed, wait, ALL_COMPLETED

def download_audio(video_url, output_path='.'):
    video = pytube.YouTube(video_url)
    stream = video.streams.filter(only_audio=True).first()
    stream.download(output_path)



def download_playlist(url, output_path='.', num_threads=5):
    playlist = Playlist(url)
    playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        executor.map(download_audio, playlist.video_urls)


if __name__ == "__main__":
    playlist_url = input("Enter YouTube playlist URL: ")
    download_path = input("Enter download path (press Enter for current directory): ")

    if not download_path:
        download_path = '.'

    download_playlist(playlist_url, download_path)
