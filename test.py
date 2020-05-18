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
chat = tele.bot.get_chat(-1001198682178)

def test(url):
	result = weibo_2_album.get(url)
	print(result.imgs)
	album_sender.send(chat, url, result)	
	
if __name__=='__main__':
	test('https://m.weibo.cn/status/J2tenmsyM')
	

# TODO: rename the module to album_sender?