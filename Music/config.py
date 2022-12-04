

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = "AQDBXxUMG9blVMXt_2KG-SZVVO8XRHUkxyuVbYthIPKNAoqFBfzAObNam1KUVp35ZGsHUlHmgVzZri-Xt50xIRuhc95oAiD6IHu71kriAhaBYtnbq-B6buf8jdaCpIuiOK9pkGI1T5u1Iwv5-ICrge9cJ2AbDUpCEw0mG1XC9hSqFyfQe5dgxhIujom-MHjl5VzMBjQIuYkNXtOUxkgJaNQwZVlUa3abS1AbblZHrF2oXh9ckb6MAHv2brHLNqgPFMqcgUV3K6Xb7JXmju3SNhU0eDish3A-xH72KXuiLS9jZtsfZKdYJq71PhTgRhOTQ9zA1LyXKkOfSaoL9Z50chuiAAAAAT853DcA"
BOT_TOKEN = "1822641510:AAFAaTnXRbtVq_PL0S6626POB92WyGWfgLw"
BOT_NAME = "Pikachu"
API_ID = "12055423"
API_HASH = "81c7d8ab7d4b5634d58006071181fbae"
OWNER_NAME = "Hayat_Murat_30"
ALIVE_NAME = "Music"
ASSISTANT_USERNAME = "Visiyv6383"
BOT_USERNAME = "Pikachu_x_bot"
ASSISTANT_NAME = "Assistant"
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/kaal0408/Music")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/d8f8fc1de9110b93ca94c.jpg")
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "https://telegra.ph/file/58da23d726b601dc3b18e.jpg")
