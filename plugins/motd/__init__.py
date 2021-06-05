import httpx
import nonebot
from nonebot import on_command
from nonebot.permission import Permission
from nonebot.typing import T_State
from adapters.cqhttp import Bot, Event
from .config import Config

global_config = nonebot.get_driver().config
plugin_config = Config(**global_config.dict())

motd = on_command("motdpe", permission=Permission(), priority=1)


@motd.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
    if args:
        state["uri"] = args  # 如果用户发送了参数则直接赋值


@motd.handle()
async def handle_second_receive(bot: Bot, event: Event, state: T_State):
    uri = state["uri"]
    if uri:
        unit = uri.split(":")
        r = httpx.post('http://api.bokro.cn/api/v1/mc/be/info', data={'host': f'{unit[0]}', 'port': f'{unit[1]}'})
        if r.json()['code'] == 200:
            await bot.send(event=event,
                           message=f"版本:{r.json()['data']['version']}\n在线玩家数:{r.json()['data']['online']}"
                                   f"/{r.json()['data']['max_player']}\n世界名称:{r.json()['data']['world_name']}\n"
                                   f"服务器标头:{r.json()['data']['server_info']}")
        else:
            await bot.send(event=event, message=f"目标服务器已关闭或找不到主机")
    else:
        await bot.send(event=event, message=f"请添加服务器地址.\n例：motdpe www.example.com:19132")
    await motd.finish()
