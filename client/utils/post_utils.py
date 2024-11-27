"""
发送相关的工具
"""
from typing import Union

import requests


def send_private_text_msg(user_id: int, msg: str) -> Union[int, None]:
    """
    发送私聊信息并返回 message_id
    """
    try:
        payload = {
            'user_id': user_id,
            'message': [{
                'type': 'text',
                'data': {
                    'text': msg
                }
            }]
        }

        response = requests.post('http://localhost:3000/send_private_msg', json=payload)
        response.raise_for_status()  # 如果 HTTP 响应状态码不是 200，引发 HTTPError

        # 转换响应为 JSON 并获取 message_id
        data = response.json()
        return data.get("message_id")

    except requests.exceptions.RequestException as e:
        print(f"请求出错: {e}")
        return None
    except ValueError:
        print("响应不是有效的 JSON")
        return None


def send_group_text_msg(group_id: int, msg: str) -> Union[int, None]:
    """
    发送群聊信息并返回 message_id
    """
    try:
        payload = {
            'group_id': group_id,
            'message': [{
                'type': 'text',
                'data': {
                    'text': msg
                }
            }]
        }

        response = requests.post('http://localhost:3000/send_group_msg', json=payload)
        response.raise_for_status()  # 如果 HTTP 响应状态码不是 200，引发 HTTPError

        # 转换响应为 JSON 并获取 message_id
        data = response.json()
        return data.get("message_id")

    except requests.exceptions.RequestException as e:
        print(f"请求出错: {e}")
        return None
    except ValueError:
        print("响应不是有效的 JSON")
        return None



# [CQ:mface,summary=&#91;哈欠&#93;,url=https://gxh.vip.qq.com/club/item/parcel/item/12/12a2308d790509abb90cafff6161d900/raw300.gif,emoji_id=12a2308d790509abb90cafff6161d900,emoji_package_id=240792,key=0dc7681880e867fc]