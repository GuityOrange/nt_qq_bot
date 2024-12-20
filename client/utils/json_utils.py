from enetity.data_enetity import MsgData

"""
解析json格式的工具
"""


def extract_message_details(json_data: dict) -> MsgData:
    """
    从 JSON 数据解析并提取发送人信息和消息内容

    :param json_data: 一个消息对象
    :return: 解析结果的列表，包含sender_id, sender_name、messages, message_type 和 group_id(可选)
    """
    try:
        # 获取发送者的 ID 和昵称
        sender_id = json_data.get("sender", {}).get("user_id", "未知ID")
        sender_name = json_data.get("sender", {}).get("nickname", "未知名称")

        # 获取消息类型
        message_type = json_data.get("message_type", "未知类型")

        # 如果是群聊类型，提取群组 ID
        group_id = None
        if message_type == "group":
            group_id = json_data.get("group_id", "未知群ID")

        # 构造提取结果
        result = {
            "target_id": sender_id,
            "sender_id": sender_id,
            "sender_name": sender_name,
            "message_type": message_type,
            "messages": json_data.get("message", []),
            "datas": json_data.get("datas", [])
        }
        if group_id:
            result["group_id"] = group_id
            result['target_id'] = group_id
        msg_data = MsgData(**result)

        return msg_data

    except Exception as e:
        print(f"解析消息时出现错误: {e}")


def wrap_as_forward_messages(messages_list: list[list[dict]]) -> list[dict]:
    """
    将消息包装为转发消息
    :param messages_list: 消息列表
    :return: 转发消息列表
    """
    if not isinstance(messages_list[0], list):
        print(f'wrap_as_forward_messages: messages_list[0] is not list')
        assert 0
    forward_messages = []
    for messages in messages_list:
        forward_messages.append({
            "type": "node",
            "data": {
                'content': messages
            }
        })
    return forward_messages


def check_equal_key_words(messages: list[dict], key_words: list[str]) -> bool:
    """
    检查是否消息文本完全匹配关键词
    """
    for message in messages:
        if message['type'] == 'text' and message['data']['text'] in key_words:
            return True
    return False

def check_part_key_words(messages: list[dict], key_words: list[str]) -> bool:
    """
    检查是否消息文本包含关键词
    """
    for message in messages:
        if message['type'] == 'text':
            for key_word in key_words:
                if key_word in message['data']['text']:
                    return True
    return False