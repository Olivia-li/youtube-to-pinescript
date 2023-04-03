import sys
from transcribe import get_transcript, get_video_id
from summarize import summarize_transcript
from pine import generate_pine_script

def process_video_to_pine_script(youtube_url):
    video_id = get_video_id(youtube_url)
    transcript_file = get_transcript(video_id)
    transcript = ''.join([entry['text'] + "\n" for entry in transcript_file])
    print(transcript)
    summary_file = summarize_transcript(transcript)
    print(summary_file)
    pine_script_file = generate_pine_script(summary_file)
    
    return pine_script_file

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <youtube_video_url>")
        sys.exit(1)

    youtube_url = sys.argv[1]
    pine_script_file = process_video_to_pine_script(youtube_url)
    print(f"Pine script generated: {pine_script_file}")