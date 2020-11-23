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
# chat = tele.bot.get_chat('@web_record')

def test(url):
	result = weibo_2_album.get(url)
	album_sender.send_v2(chat, result, send_all=True, time_sleep=5)	

def testPicBot():
	result = Result()
	result.cap_html = 'test'
	print(result)
	r = album_sender.send_v2(chat, result, send_all=True, time_sleep=5)	
	print(r)
	
if __name__=='__main__':
	# test('https://www.douban.com/people/2627485/status/3185647338/')
	# test('https://www.douban.com/people/60997951/status/3185239306/')
	test('https://m.weibo.cn/status/Ju87E3Hms')