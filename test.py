#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import album_sender
import weibo_2_album
import web_2_album
import yaml
from telegram_util import AlbumResult as Result
from telegram.ext import Updater

with open('CREDENTIALS') as f:
	CREDENTIALS = yaml.load(f, Loader=yaml.FullLoader)
tele = Updater(CREDENTIALS['bot_token'], use_context=True)
# chat = tele.bot.get_chat(-1001198682178)
# chat = tele.bot.get_chat(-1001198682178)
chat = tele.bot.get_chat('@web_record')

def test(url):
	result = web_2_album.get(url)
	album_sender.send_v2(chat, result, send_all=True, time_sleep=5)	

def testPicBot():
	result = Result()
	result.imgs = ['']
	album_sender.send_v2(chat, result, send_all=True, time_sleep=5)	
	
if __name__=='__main__':
	testPicBot()
	

# TODO: rename the module to album_sender?