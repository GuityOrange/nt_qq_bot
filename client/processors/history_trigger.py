import asyncio

from enetity.data_enetity import MsgData
from enetity.history_enetity import HistoryManager
from event.plus_one_event import event_for_text_one_plus

HISTORY_MANAGER = HistoryManager()

"""
data:
target_id: 目标ID
sender_id: 发送者ID
sender_name: 发送者名称
messages: 消息列表
datas: 详细的消息列表
message_type: 消息类型
group_id: 群聊ID (可选)
"""

async def history_trigger(data: MsgData) -> None:
    """
    通过关键词触发的事件
    """
    HISTORY_MANAGER.update(data.message_type, data.target_id, data.messages)

    asyncio.create_task(event_for_text_one_plus(data, HISTORY_MANAGER))