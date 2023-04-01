import sys
import os
from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi

urls = [
    'https://www.youtube.com/watch?v=cbGM4Bpa0eg',
    'https://www.youtube.com/watch?v=XD3rQQTFdVY',
    'https://www.youtube.com/watch?v=h4JpQ94M4X4&authuser=0',
    'https://www.youtube.com/watch?v=46ZXuak9oB0&authuser=0',
    'https://www.youtube.com/watch?v=jXcegYhNCLo&authuser=0',
    'https://www.youtube.com/watch?v=uN3i-Cihjm8&authuser=0',
    'https://www.youtube.com/watch?v=ptLBzmUmeRk&authuser=0'
]


def get_video_id(url):
    return url.split("watch?v=")[-1]


def get_video_title(video_id):
    try:
        yt = YouTube(f"https://www.youtube.com/watch?v={video_id}")
        return yt.title
    except Exception as e:
        print(f"An error occurred while fetching the video title: {e}")
        return None


def get_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return transcript
    except Exception as e:
        print(f"An error occurred while fetching the transcript: {e}")
        return None


def save_transcript(transcript, video_title):
    filename = f"{video_title}.txt"
    filepath = os.path.join(f'{os.path.dirname(os.path.realpath(__file__))}/transcriptions', filename)
    with open(filepath, "w", encoding="utf-8") as file:
        for entry in transcript:
            file.write(entry['text'] + "\n")
    print(f"Transcript saved as '{filename}'")


def main():
    # if len(sys.argv) < 2:
    #     print("Usage: python script.py <youtube_url>")
    #     sys.exit(1)

    for item in urls:
        youtube_url = item

        # youtube_url = sys.argv[1]
        video_id = get_video_id(youtube_url)
        video_title = get_video_title(video_id)
        transcript = get_transcript(video_id)

        if transcript and video_title:
            save_transcript(transcript, video_title)


if __name__ == "__main__":
    main()