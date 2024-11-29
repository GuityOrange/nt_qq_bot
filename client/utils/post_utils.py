"""
发送相关的工具
"""
from typing import Union

from utils.json_utils import wrap_as_forward_messages

import requests


def send_msg(messages: list, target_id: int, target_type: str, forward_msg_flag:bool = False) -> Union[int, None]:
    """
    发送消息并返回 message_id
    """
    try:
        if forward_msg_flag:
            url = f'http://localhost:3000/send_{target_type}_forward_msg'
            payload = {
                'messages': messages
            }
        else:
            url = f'http://localhost:3000/send_{target_type}_msg'
            payload = {
                'message': messages
            }

        if target_type == 'private':
            payload['user_id'] = target_id
        elif target_type == 'group':
            payload['group_id'] = target_id
        else:
            print("未知的目标类型")
            return None

        response = requests.post(url, json=payload)
        response.raise_for_status()  # 如果 HTTP 响应状态码不是 200，引发 HTTPError

        # 转换响应为 JSON 并获取 message_id
        data = response.json()
        if data.get("status") == "failed":
            print(f"发送消息失败")
            print(data)
            return None
        return data.get("message_id")

    except requests.exceptions.RequestException as e:
        print(f"请求出错: {e}")
        return None
    except ValueError:
        print("响应不是有效的 JSON")
        return None


def send_text_msg(target_id: int, message_type: str, msg: str, forward_msg_flag:bool = False) -> Union[int, None]:
    """
    发送文本消息并返回 message_id
    """
    data = {
        'type': 'text',
        'data': {
            'text': msg
        }
    }
    msg = [data]
    if forward_msg_flag:
        msg = wrap_as_forward_messages([msg])
    return send_msg(msg, target_id, message_type, forward_msg_flag)

def send_at_text_msg(target_id: int, message_type: str, msg: str, sender_id: int, forward_msg_flag: bool = False) -> Union[int, None]:
    """
    发送@某人的信息并加上文本消息并返回 message_id
    """
    at_msg = {
        "type": "at",
        "data": {
            "qq": sender_id,
            "name": ""
        }
    }
    text_msg = {
        'type': 'text',
        'data': {
            'text': msg,
        }
    }

    msg = [at_msg, text_msg]
    if forward_msg_flag:
        msg = wrap_as_forward_messages([msg])

    return send_msg(msg, target_id, message_type, forward_msg_flag)


def send_mface_msg(target_id: int, message_type: str, summary: str, url: str, emoji_id: str, emoji_package_id: int, key: str) -> Union[int, None]:
    """
    发送动画表情并返回 message_id
    """
    data = {
        'type': 'mface',
        'data': {
            'summary': summary,
            'url': url,
            'emoji_id': emoji_id,
            'emoji_package_id': emoji_package_id,
            'key': key
        }
    }
    return send_msg([data], target_id, message_type)


# [{'type': 'mface', 'data': {'summary': '[哈欠]', 'url': 'https://gxh.vip.qq.com/club/item/parcel/item/12/12a2308d790509abb90cafff6161d900/raw300.gif', 'emoji_id': '12a2308d790509abb90cafff6161d900', 'emoji_package_id': 240792, 'key': '0dc7681880e867fc'}}]
# [CQ:mface,summary=&#91;哈欠&#93;,url=https://gxh.vip.qq.com/club/item/parcel/item/12/12a2308d790509abb90cafff6161d900/raw300.gif,emoji_id=12a2308d790509abb90cafff6161d900,emoji_package_id=240792,key=0dc7681880e867fc]