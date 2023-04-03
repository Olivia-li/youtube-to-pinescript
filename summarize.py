import openai
import os
import sys
from dotenv import load_dotenv

# Load the OpenAI API key from a .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

# Set the directory paths
transcriptions_path = "transcriptions"
summarizations_path = "summarization"


def read_transcript(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def summarize_transcript(transcript):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = [{"role": "system", "content" : "You are a summarizer bot designed to write easy to read blog articles from Youtube transcripts. The transcript will be provided in square brackets. Do not leave any detail out but be as clear as possible. These are educational blogs where you want to teach the reader what is being taught in these videos. Be as accurate but also as concise as possible."},
        {"role": "user", "content" : f'Summarize the following:\n\n[{transcript}]'}],
        max_tokens=1500,
        n=1,
        stop=None,
        temperature=0.5,
    )

    summary = response.choices[0].message.content.strip()
    return summary



def save_summary(summary, file_name):
    if not os.path.exists(summarizations_path):
        os.makedirs(summarizations_path)

    file_path = os.path.join(summarizations_path, file_name)
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(summary)
    print(f"Summary saved as '{file_name}'")

def run_summarization(file_name):
    print(f"Summarizing '{file_name}'...")
    transcript_path = os.path.join(transcriptions_path, file_name)
    transcript = read_transcript(transcript_path)
    summary = summarize_transcript(transcript)
    save_summary(summary, file_name)


def main():
    if not os.path.exists(transcriptions_path):
        print(f"No transcriptions directory found at '{transcriptions_path}'")
        sys.exit(1)

    # If there is a argv then summarize file by argv. If not go through entire summarization folder
    if len(sys.argv) > 1:
        file_name = os.path.basename(sys.argv[1])
        run_summarization(file_name)
    else:
        print(f"No file name provided. Summarizing all files in '{transcriptions_path}'")
        for file_name in os.listdir(transcriptions_path):
            if file_name.endswith(".txt"):
                run_summarization(file_name) 

    return os.path.join(summarizations_path, file_name)

if __name__ == "__main__":
    main()