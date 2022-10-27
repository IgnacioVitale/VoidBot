# Void-Bot

### _A Discord bot powered by Python_

### Setup

- Install python 3.8 or higher
- Install git
- Install discord.py
  ```sh
  py -m pip install -U discord.py
  py -m pip install -U discord.py[voice]
  ```
- Install other dependencies
  ```sh
    py -m pip install python-dotenv
    py -m pip install youtube_dl
  ```
- Create a .env file and ask for the bot key and the json key
- Download the ffmpeg-master-latest-win64-gpl.zip package from https://github.com/BtbN/FFmpeg-Builds/releases
- Uncompress the file and change the name of the folder to ffmpeg
- Add to the PATH in environment variables the path to said folder/bin, eg:
  C:\ffmpeg\bin

### How to run

Open a terminal in the bot folder
Run the following command: py -3 test_bot.py

### Resources

https://discordpy.readthedocs.io/en/latest/index.html \
https://discordpy.readthedocs.io/en/stable/api.html#messages \
https://jsonbin.io/api-reference/bins/read
