import openai
import os
import sys
from dotenv import load_dotenv

# Load the OpenAI API key from a .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

# Set the directory paths
summarizations_path = "summarization"
scripts_path = "scripts"


def read_summary(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def generate_pine_script(summary):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = [{"role": "system", "content" : "You are a Pine script generator for TradingView. You take a summary of a trading strategy and return a complete Pine script that implements that strategy. Be sure to implement the complete strategy that is given to you."},
        {"role": "user", "content" : f'Create a Pine script for the following strategy:\n\n[{summary}]'}],
        max_tokens=2000,
        n=1,
        stop=None,
        temperature=0.5,
    )

    script = response.choices[0].message.content.strip()
    return script



def save_script(script, file_name):
    if not os.path.exists(scripts_path):
        os.makedirs(scripts_path)

    file_path = os.path.join(scripts_path, file_name)
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(script)
    print(f"Script saved as '{file_name}'")

def run_script_generation(file_name):
    print(f"Generating script for '{file_name}'...")
    summary_path = os.path.join(summarizations_path, file_name)
    summary = read_summary(summary_path)
    script = generate_pine_script(summary)
    save_script(script, file_name)


def main():
    if not os.path.exists(summarizations_path):
        print(f"No summarizations directory found at '{summarizations_path}'")
        sys.exit(1)

    # if len(sys.argv) > 1:
    #     if sys.argv[1].endswith(".txt"):
    #         print(sys.argv[1])
    #         run_script_generation(sys.argv[1])
    # else:
    for file_name in os.listdir(summarizations_path):
        if file_name.endswith(".txt"):
            run_script_generation(file_name)


if __name__ == "__main__":
    main()