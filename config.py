from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("12670454", ""))
API_HASH = getenv("d64ac938b92d86089fd5690a2cbb5417", "")
BOT_TOKEN = getenv("5266153278:AAERJCpK8hOvcyv_1CdUAL7DbygvYpU8HLg")
BOT_NAME = getenv(""🇧𝐄𝐒𝐓𝐈𝐄𝐒 🇫𝐎𝐑 🇹𝐇𝐄 🇷𝐄𝐒𝐓𝐈𝐄𝐒"")
BOT_USERNAME = getenv(""besties1bot "")
OWNER_USERNAME = getenv(""kishnu123 "")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "DevilsHeavenMF")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
START_IMG = getenv("START_IMG", "https://telegra.ph/file/89cbc8b8760b6abff430f.jpg")
PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/89cbc8b8760b6abff430f.jpg")
SESSION_NAME = getenv("1BVtsOHgBu8Gs8lbezkPiYCyCQGrVrYCdcav5UiHsszyC8AY96I_MX74o9kXdMjP6N3c80j-jxI5WGvzONe3EFbtgtOEXKDlDTgDi5ruGF-9yeEUQZV1W-rhJpY6wND3e6CRgLObVwSKM-9kNvg64GY5eO9TebXjHwgfuuf9C27-3tHbpWAU6rI5vaiduHL-Qf0bY_2cOU4uy588kfo57H-DlIAOUmtj6VrhDsQRG5et83pSvM85Kqkb7gr-Qvg6K8aNBNRDuI1fNCpO_gnFUS4kntmPBMUzQcjPbNz4vDEqvFqNcMqErS9saHVPe8bHsbbmzlcQRkoloAHH7RL-kmkzfXECaoZc= 
", )
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", " /   ").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("S", 5161343935 "").split()))
