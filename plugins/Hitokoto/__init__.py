import json
import requests
import nonebot
from nonebot import on_command
from nonebot.permission import Permission
from nonebot.adapters import Bot, Event
from .config import Config

global_config = nonebot.get_driver().config
plugin_config = Config(**global_config.dict())
#输入yy，即刻获得经典名言(doge
hitokoto = on_command("yy", permission=Permission(), priority=1)


@hitokoto.handle()
async def handler(bot: Bot, event: Event):
    rturn = requests.get("https://v1.hitokoto.cn/?c=a")
    ref = json.loads(rturn.text)
    print(ref)
    await bot.send(event=event, message=f"{ref['hitokoto']}\nFrom:{ref['from']}")
    await hitokoto.finish()
