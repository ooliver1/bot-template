# SPDX-License-Identifier: MIT

from botbase import Emojis


# db_enabled = False  # default  # FIXME: enable when setup
# db_url = "postgres://usrname:passwd@ip.addr/botname"  # for dev
# db_name = "botname"  # FIXME: botname
# db_user = "ooliver"  # default
# db_host = "localhost"  # default
# version = "0.0.0"  # default
# aiohttp_enabled = True  # default
# colors = [0x9966cc]  # default
# blacklist_enabled = True  # default
prefix = ["!"]  # FIXME: actual prefix
# help_msg = """
# HI! Welcome to the help page for {name}!
# Use `{prefix}help <command>` for more info on a command,
# or `{prefix}help <category>` for more info on a category,
# Use the dropdown below to select a category.
# Have fun!
# """  # default
# helpindex = """
# I have been up since {created_at} and I serve for you!
# """  # default
# helptitle = "Help Me {name}!"  # default
# helpfields = {}  # default
# helpinsert = ""  # default
emojiset = Emojis({"in/dex": "..."})  # FIXME: emoji set for help select
# logchannel = None  # default
# guild_ids = None  # default
