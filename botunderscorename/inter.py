from botbase import MyInter

from .bot import BotName


# Ideally a type alias but nextcord broken right now.
class Inter(MyInter[BotName]):
    ...
