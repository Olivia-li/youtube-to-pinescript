# Youtube to Pine Script
Turn any Youtube video about creating a TradingView indicators into a pine script with ChatGPT

## Get a OpenAI API key
Create an account at [platform.openai.com](https://platform.openai.com) and click on `View API` keys in your profile settings.
```
$ mv .env.example .env
```
Go into the .env file and add your OPENAI key that you generated on the OpenAI website
<img width="1063" alt="image" src="https://user-images.githubusercontent.com/9896624/229427078-c3adf157-3cde-4b61-a8db-5714fd061c50.png">


## Setup
```
$ git clone https://github.com/Olivia-li/youtube-to-pinescript.git
$ source bin/activate
$ pip3 install -r requirements.txt
$ python3 main.py <YOUTUBE URL>
```

Your pine script will be stored in the `./scripts` directory
