#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import album_sender
import web_2_album
import yaml
from telegram_util import AlbumResult as Result
from telegram.ext import Updater

with open('CREDENTIALS') as f:
	CREDENTIALS = yaml.load(f, Loader=yaml.FullLoader)
tele = Updater(CREDENTIALS['bot_token'], use_context=True)
chat = tele.bot.get_chat(-1001198682178)

def test(url):
	result = web_2_album.get(url)
	album_sender.send(chat, url, result)	
	
if __name__=='__main__':
	# test('https://www.douban.com/people/46037668/status/2956088549/')
	# test('https://www.douban.com/people/kinokinokino/status/2947364315/')
	result = Result()
	result.imgs = ['https://mmbiz.qpic.cn/mmbiz_gif/e6dIc6Q5sLqCfv4giajNtn9KHNr8Xrx1sGEXfY3ToebCyCIl7ia1OHdQC5G71vVwiaRkTFXxVdS28tQ40T8Yld86g/640?wx_fmt=gif', 'https://mmbiz.qpic.cn/mmbiz_png/e6dIc6Q5sLoTzby70dnXeV3QOV35JbakDan0eYv6yJd3bvtqeiaLNibvvCf4ic5zLsooHuEicP0uzOs6spTicTG753w/640?wx_fmt=png', 'https://mmbiz.qpic.cn/mmbiz_png/e6dIc6Q5sLoTzby70dnXeV3QOV35JbakOcnbJR9n1DMuIXdzg0Qy1L3VAAcrlQGtBbuiawbAicVvv4ejELoSFUEA/640?wx_fmt=png', 'https://mmbiz.qpic.cn/mmbiz_png/e6dIc6Q5sLoTzby70dnXeV3QOV35JbakPaPSy4GkldFtQNbknefn7R6icIYhvnOEcu5oc3nTjJ1pibOjrMT66uAA/640?wx_fmt=png', 'https://mmbiz.qpic.cn/mmbiz_png/e6dIc6Q5sLoTzby70dnXeV3QOV35JbakERbBOgBkwJvklP7O7l5ZDR3l4lmFVXXz4H092GOVeFUGUahT9vtOPA/640?wx_fmt=png', 'https://mmbiz.qpic.cn/mmbiz_png/e6dIc6Q5sLoTzby70dnXeV3QOV35Jbakrg72PTxLEb0QWN4rq2bBmy3288PEbVCFLjVsmUSsDSVKQaXpwHbzcA/640?wx_fmt=png', 'https://mmbiz.qpic.cn/mmbiz_png/e6dIc6Q5sLoTzby70dnXeV3QOV35JbakQUJCwMUcibkfUicxwFYhnaTsF38J8ZADXQBdCoKMs8pH75rGSEKEhDIA/640?wx_fmt=png', 'https://mmbiz.qpic.cn/mmbiz_png/e6dIc6Q5sLoTzby70dnXeV3QOV35JbakAI4J6VxvRGGichpHZCibnBpSg3wnm2HlajjCtW4Or1bKxf2ruEbNfTZQ/640?wx_fmt=png', 'https://mmbiz.qpic.cn/mmbiz_png/e6dIc6Q5sLoTzby70dnXeV3QOV35JbakQViamALNue8FPPbqWqoT6bGLXVrJRQVp7kX5z7WVseZMLfibALaBfWPw/640?wx_fmt=png', 'https://mmbiz.qpic.cn/mmbiz_png/e6dIc6Q5sLoTzby70dnXeV3QOV35JbakjRTvooO01ia8hxbPuzTKxI5Yiaqg6S7wmPcnTMDKAUJHjfAnVTHqFbFA/640?wx_fmt=png', 'https://mmbiz.qpic.cn/mmbiz_png/e6dIc6Q5sLoTzby70dnXeV3QOV35Jbak8KJ0ibleGbX6cJlySvc4A3Wb5Sh4qbicN1brKo2expHd6dVGebsZgKHA/640?wx_fmt=png', 'https://mmbiz.qpic.cn/mmbiz_png/e6dIc6Q5sLoAFc3BPqsTicic55loUJXibLZj8zv7TAia0EYa4tYAr1qRjRcKnYMfc9y2TibHJpZdAKORxQBqqcPa2jg/640?wx_fmt=png']
	album_sender.send(chat, '', result)
	

# TODO: rename the module to album_sender?