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

def test(url):
	result = web_2_album.get(url)
	album_sender.send(chat, url, result)	
	
if __name__=='__main__':
	test('https://www.douban.com/people/68848724/status/2942117860')
	# test('https://www.douban.com/people/kinokinokino/status/2947364315/')
	

# TODO: rename the module to album_sender?