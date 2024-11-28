from typing import Optional

from pydantic import BaseModel

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

class MsgData(BaseModel):
    target_id: int
    sender_id: int
    sender_name: str
    messages: list
    datas: list
    message_type: str
    group_id: Optional[int] = None