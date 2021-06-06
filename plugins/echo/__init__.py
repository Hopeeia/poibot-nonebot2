import nonebot
from nonebot import on_command
from nonebot.permission import Permission

from adapters.cqhttp import Bot, MessageEvent
from .config import Config

global_config = nonebot.get_driver().config
plugin_config = Config(**global_config.dict())

echo = on_command("echo", permission=Permission(), priority=1)


# 输入echo加上你要说的话，bot就是复读机

@echo.handle()
async def echo_escape(bot: Bot, event: MessageEvent):
    await bot.send(message=event.get_message(), event=event)
    await bot.finish()
