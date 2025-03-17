from astrbot.api.event import filter
from astrbot.api.all import *
from typing import (Dict, Any, Optional, AnyStr, Callable, Union, Awaitable,Coroutine)
import os
import json
from data.plugins.astrbot_plugin_emoji import emoji
from astrbot.api.provider import ProviderRequest
from astrbot.core.platform.sources.aiocqhttp.aiocqhttp_message_event import AiocqhttpMessageEvent
from pathlib import Path
from typing import Dict, List
from astrbot.api.all import *
from astrbot.api.event import filter, AstrMessageEvent
import random
MESSAGE_BUFFER: Dict[str, List[dict]] = {}  # {group_id: [{"user_id": str, "messages": list}, ...]}
BUFFER_LIMIT = 2  # 一问一答的对话对数量
MERGE_TIMEOUT = 60  # 同一用户消息合并时间窗口（秒）




@register("astrbot_plugin_emoji", "KurisuRee7", 
          "发送指令@小伙伴以创建一个表情包",
          "v1.0.0", "repo url")
class Emoji(Star):
    def __init__(self, context: Context, config: AstrBotConfig):
        super().__init__(context)
        self.config = config

    @filter.command("表情包")
    async def list(self, event: AstrMessageEvent):
       yield event.plain_result(
            "指令格式：@本机器人 指令@xx\n"
            "支持的指令：摸头 感动哭了 膜拜 咬 \n"
            "可莉吃 捣 咸鱼 玩 拍 丢 撕 求婚  \n"
            "爬 你可能需要他 想看 点赞        "
        ) 

    @filter.command("摸头")
    async def emoji1(self, event: AstrMessageEvent):
        ids = await emoji.parse_target(event)
        data = await emoji.fetch_image(ids, "摸头")
        await event.send(data)
    @filter.command("感动哭了")
    async def emoji2(self, event: AstrMessageEvent):
        ids = await emoji.parse_target(event)
        data = await emoji.fetch_image(ids, "感动哭了")
        await event.send(data)
    @filter.command("膜拜")
    async def emoji3(self, event: AstrMessageEvent):
        ids = await emoji.parse_target(event)
        data = await emoji.fetch_image(ids, "膜拜")
        await event.send(data)
    @filter.command("咬")
    async def emoji4(self, event: AstrMessageEvent):
        ids = await emoji.parse_target(event)
        data = await emoji.fetch_image(ids, "咬")
        await event.send(data)
    @filter.command("可莉吃")
    async def emoji5(self, event: AstrMessageEvent):
        ids = await emoji.parse_target(event)
        data = await emoji.fetch_image(ids, "可莉吃")
        await event.send(data)
    # @filter.command("吃掉")
    # async def emoji6(self, event: AstrMessageEvent):
    #     ids = await emoji.parse_target(event)
    #     data = await emoji.fetch_image(ids, "吃掉")
    #     await event.send(data)
    @filter.command("捣")
    async def emoji7(self, event: AstrMessageEvent):
        ids = await emoji.parse_target(event)
        data = await emoji.fetch_image(ids, "捣")
        await event.send(data)
    @filter.command("咸鱼")
    async def emoji8(self, event: AstrMessageEvent):
        ids = await emoji.parse_target(event)
        data = await emoji.fetch_image(ids, "咸鱼")
        await event.send(data)
    @filter.command("玩")
    async def emoji9(self, event: AstrMessageEvent):
        ids = await emoji.parse_target(event)
        data = await emoji.fetch_image(ids, "玩")
        await event.send(data)
    @filter.command("拍")
    async def emoji11(self, event: AstrMessageEvent):
        ids = await emoji.parse_target(event)
        data = await emoji.fetch_image(ids, "拍")
        await event.send(data)
    @filter.command("丢")
    async def emoji12(self, event: AstrMessageEvent):
        ids = await emoji.parse_target(event)
        data = await emoji.fetch_image(ids, "丢")
        await event.send(data)
    @filter.command("撕")
    async def emoji13(self, event: AstrMessageEvent):
        ids = await emoji.parse_target(event)
        data = await emoji.fetch_image(ids, "撕")
        await event.send(data)
    @filter.command("求婚")
    async def emoji14(self, event: AstrMessageEvent):
        ids = await emoji.parse_target(event)
        data = await emoji.fetch_image(ids, "求婚")
        await event.send(data)
    @filter.command("爬")
    async def emoji15(self, event: AstrMessageEvent):
        ids = await emoji.parse_target(event)
        data = await emoji.fetch_image(ids, "爬")
        await event.send(data)
    @filter.command("你可能需要他")
    async def emoji16(self, event: AstrMessageEvent):
        ids = await emoji.parse_target(event)
        data = await emoji.fetch_image(ids, "你可能需要他")
        await event.send(data)
    @filter.command("想看")
    async def emoji17(self, event: AstrMessageEvent):
        ids = await emoji.parse_target(event)
        data = await emoji.fetch_image(ids, "想看")
        await event.send(data)
    @filter.command("点赞")
    async def emoji18(self, event: AstrMessageEvent):
        ids = await emoji.parse_target(event)
        data = await emoji.fetch_image(ids, "点赞")
        await event.send(data)