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
	url = 'http://weibointl.api.weibo.cn/share/131595305.html'
	result = web_2_album.get(url)
	album_sender.send(chat, url, result, rotate=True)

	url = 'http://www.douban.com/people/RonaldoLuiz/status/2877273534/'
	result = web_2_album.get(url)
	album_sender.send(chat, url, result)

	url = 'https://weibointl.api.weibo.cn/share/133847669.html?weibo_id=4468334634971089&from=groupmessage&isappinstalled=0'
	result = web_2_album.get(url)
	album_sender.send(chat, url, result)	

# TODO: rename the module to album_sender?