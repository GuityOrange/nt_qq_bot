from utils.post_utils import send_group_text_msg, send_private_text_msg

"""
通过关键词来触发的事件
data:
sender_id: 发送者ID
sender_name: 发送者名称
messages: 消息列表
message_type: 消息类型
group_id: 群聊ID (可选)
"""

def event_kw_hello_world(data: dict) -> None:
    """
    通过关键词触发的事件
    """
    messages = data.get("messages", [])
    message_type = data.get("message_type", "未知类型")

    if message_type == "private":
        for message in messages:
            if "hello" in message:
                send_private_text_msg(data["sender_id"], "Hello World!")
                print(f'Hello World! to {data["sender_id"]}')
                return
    elif message_type == "group":
        for message in messages:
            if "hello" in message:
                send_group_text_msg(data["group_id"], "Hello World!")
                print(f'Hello World! to {data["group_id"]}')
                return
