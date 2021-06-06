import nonebot
from nonebot import on_command
from nonebot.permission import Permission
from adapters.cqhttp import Bot, Event
from .config import Config

global_config = nonebot.get_driver().config
plugin_config = Config(**global_config.dict())

ahelp = on_command("help", permission=Permission(), priority=1)
#帮助

@ahelp.handle()
async def help_escape(bot: Bot, event: Event):
    await bot.send(message=f"目前支持的使用方法有:\n"
                           f"1.一言\n  发送yy即可\n"
                           f"2.mc基岩版服务器信息查询\n  发送motdpe+地址:端口即可\n"
                           f"3.bot复读机(doge\n  输入echo+你要说的话\n"
                           f"特别鸣谢:感谢丁石大佬提供的查询api", event=event)
