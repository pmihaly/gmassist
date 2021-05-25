from blocks import date, greeting, weather
import yaml
from gtts import gTTS
import datetime


def write_mp3(text):
    with open(f"speeches/{datetime.date.today().strftime('%Y-%m-%d')}.mp3", "wb") as file:
        gTTS(text, lang='hu').write_to_fp(file)

    quit()


with open("config.yaml", "r") as config:
    try:
        CONFIG = yaml.safe_load(config)

    except yaml.YAMLError:
        write_mp3("A konfigurációs fájl szintaxisa helytelen. ")


SAYSTRING = ""
SAYSTRING += greeting.say(CONFIG)
SAYSTRING += date.say(CONFIG)
SAYSTRING += weather.say(CONFIG)

write_mp3(SAYSTRING)
