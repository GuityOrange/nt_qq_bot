import requests


def test_post_forward_msg():
    test_payload = {
        'group_id': 664289892,
        'message': [
            {
                "type": "forward",
                "data": {
                    'id': '7442731747587531974'
                }
            }
        ]
    }
    url = f'http://localhost:3000/send_group_msg'

    response = requests.post(url, json=test_payload)
    response.raise_for_status()  # 如果 HTTP 响应状态码不是 200，引发 HTTPError

    # 转换响应为 JSON 并获取 message_id
    data = response.json()
    if data.get("status") == "failed":
        print(f"发送消息失败")
        print(data)
        return None


def test_get_forward_msg():
    url = f'http://localhost:3000/get_forward_msg?id=7442731747587531974'

    response = requests.get(url)
    response.raise_for_status()  # 如果 HTTP 响应状态码不是 200，引发 HTTPError

    # 转换响应为 JSON 并获取 message_id
    data = response.json()
    print(data)
    if data.get("status") == "failed":
        print(f"获取消息失败")
        print(data)
        return None