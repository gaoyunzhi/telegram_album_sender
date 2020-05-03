#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import album_sender
import web_2_album
import yaml
from telegram.ext import Updater

with open('CREDENTIALS') as f:
	CREDENTIALS = yaml.load(f, Loader=yaml.FullLoader)
tele = Updater(CREDENTIALS['bot_token'], use_context=True)
chat = tele.bot.get_chat(-1001198682178)
	
if __name__=='__main__':
	url = 'https://www.douban.com/people/68848724/status/2942117860/'
	result = web_2_album.get(url)
	album_sender.send(chat, url, result)	

# TODO: rename the module to album_sender?