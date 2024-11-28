import asyncio

from enetity.data_enetity import MsgData
from event.key_word_event import event_kw_hello_world, event_kw_mface, event_kw_good_morning

async def keyword_test_trigger(data: MsgData) -> None:
    """
    通过关键词触发的事件
    """
    asyncio.create_task(event_kw_hello_world(data))
    asyncio.create_task(event_kw_mface(data))
    asyncio.create_task(event_kw_good_morning(data))
