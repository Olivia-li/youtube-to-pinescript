import sys
from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi


def get_video_id(url):
    return url.split("watch?v=")[-1]


def get_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return transcript
    except Exception as e:
        print(f"An error occurred while fetching the transcript: {e}")
        return None


def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <youtube_url>")
        sys.exit(1)

    youtube_url = sys.argv[1]
    video_id = get_video_id(youtube_url)
    transcript = get_transcript(video_id)

    if transcript:
        print("Transcript:")
        for entry in transcript:
            print(entry['text'])


if __name__ == "__main__":
    main()