from pytubefix import YouTube
import os
import re
from moviepy import VideoFileClip, AudioFileClip

# Function to sanitize filenames (removes invalid characters)
def sanitize_filename(title):
    return re.sub(r'[<>:"/\\|?*]', '', title)

# Function to merge video and audio
#def merge_video_audio(video_path, audio_path, output_path):
#    video_clip = VideoFileClip(video_path)
#    audio_clip = AudioFileClip(audio_path)
#
#    final_clip = video_clip.set_audio(audio_clip)  # Merge audio
#    final_clip.write_videofile(output_path, codec="libx264", audio_codec="aac", audio_bitrate="128k")

def merge_video_audio(video_path, audio_path, output_path):
    video_clip = VideoFileClip(video_path)
    audio_clip = AudioFileClip(audio_path)
    final_clip = video_clip.with_audio(audio_clip)  # ✅ Use `with_audio`
    final_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")
    # Close clips to free memory
    video_clip.close()
    audio_clip.close()

# Function to download video
def download_video(url, save_path="."):
    video = YouTube(url)

    # Get highest quality video (without audio)
    video_stream = video.streams.filter(adaptive=True, file_extension="mp4").order_by("resolution").desc().first()

    # Get highest quality audio
    audio_stream = video.streams.filter(only_audio=True, file_extension="mp4").first()

    print(f"Downloading Video: {video.title} ({video_stream.resolution})")

    # Sanitize filename
    safe_title = sanitize_filename(video.title)
    video_filename = f"{safe_title}_video.mp4"
    audio_filename = f"{safe_title}_audio.mp4"
    output_filename = f"{safe_title}.mp4"

    video_path = video_stream.download(output_path=save_path, filename=video_filename)
    audio_path = audio_stream.download(output_path=save_path, filename=audio_filename)

    # Merge video and audio
    output_path = os.path.join(save_path, output_filename)
    merge_video_audio(video_path, audio_path, output_path)

    # Remove temporary files
    os.remove(video_path)
    os.remove(audio_path)

    print("Download completed successfully!")

if __name__ == "__main__":
    video_url = input("Enter YouTube video URL: ")
    download_video(video_url)
