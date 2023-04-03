# YouTube to Pine Script Converter

This project allows you to convert any YouTube video about creating TradingView indicators into a Pine Script using ChatGPT, powered by OpenAI. Follow the step-by-step instructions below to set up and run the project.

## Prerequisites

1. Obtain an OpenAI API key: Create an account at [platform.openai.com](https://platform.openai.com) and click on "View API keys" in your profile settings.
<img width="1063" alt="image" src="https://user-images.githubusercontent.com/9896624/229427078-c3adf157-3cde-4b61-a8db-5714fd061c50.png">

## Setup

1. Clone the repository:
```
git clone https://github.com/Olivia-li/youtube-to-pinescript.git
```
2. Create a copy of the `.env.example` file and rename it to `.env`:
```
$ mv .env.example .env
```
3. Open the `.env` file and add your OpenAI API key that you generated on the OpenAI website:
```
OPENAI_API_KEY=<your_api_key_here>
```
4. Activate the virtual environment:
```
$ source bin/activate
```
5. Install the required dependencies:
```
$ pip3 install -r requirements.txt
```
6. Run the program with the YouTube URL of the video about creating a TradingView indicator:
```
$ python3 main.py <YOUTUBE_URL>
```
Your Pine Script will be stored in the `./scripts` directory.
