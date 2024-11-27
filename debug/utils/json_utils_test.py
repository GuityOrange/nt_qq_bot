import pytest
from utils.json_utils import extract_message_details  # 请替换为实际方法所在的模块名

# 定义测试函数
def test_extract_message_details():
    # 示例输入
    json_data_list = [
        # 正常文本消息
        {
            'self_id': 574306394,
            'user_id': 2026928559,
            'time': 1732725534,
            'message_id': 460998776,
            'real_id': 460998776,
            'message_seq': 460998776,
            'message_type': 'private',
            'sender': {'user_id': 2026928559, 'nickname': '途淄', 'card': ''},
            'raw_message': '11',
            'font': 14,
            'sub_type': 'friend',
            'message': [{'type': 'text', 'data': {'text': '11'}}],
            'message_format': 'array',
            'post_type': 'message'
        },
        # 带表情的消息
        {
            'self_id': 574306394,
            'user_id': 2026928559,
            'time': 1732725605,
            'message_id': 196433295,
            'real_id': 196433295,
            'message_seq': 196433295,
            'message_type': 'private',
            'sender': {'user_id': 2026928559, 'nickname': '途淄', 'card': ''},
            'raw_message': '你是？[CQ:face,id=311]',
            'font': 14,
            'sub_type': 'friend',
            'message': [
                {'type': 'text', 'data': {'text': '你是？'}},
                {'type': 'face', 'data': {'id': '311'}}
            ],
            'message_format': 'array',
            'post_type': 'message'
        },
        # 包含图片的消息
        {
            'self_id': 574306394,
            'user_id': 2026928559,
            'time': 1732725656,
            'message_id': 911973443,
            'real_id': 911973443,
            'message_seq': 911973443,
            'message_type': 'private',
            'sender': {'user_id': 2026928559, 'nickname': '途淄', 'card': ''},
            'raw_message': '你是[CQ:image,file=73910DB31C4D9DBC83363BB038A2AC6B.png,subType=0,url=https://example.com/image.png,file_size=35723]',
            'font': 14,
            'sub_type': 'friend',
            'message': [
                {'type': 'text', 'data': {'text': '你是'}},
                {'type': 'image', 'data': {'file': '73910DB31C4D9DBC83363BB038A2AC6B.png',
                                           'subType': 0,
                                           'url': 'https://example.com/image.png',
                                           'file_size': '35723'}}
            ],
            'message_format': 'array',
            'post_type': 'message'
        }
    ]

    # 预期输出
    expected_result = [
        {
            "sender_id": 2026928559,
            "sender_name": "途淄",
            "messages": ["11"]
        },
        {
            "sender_id": 2026928559,
            "sender_name": "途淄",
            "messages": ["你是？", "[表情: 311]"]
        },
        {
            "sender_id": 2026928559,
            "sender_name": "途淄",
            "messages": ["你是", "[图片: https://example.com/image.png]"]
        }
    ]

    # 调用被测函数
    actual_result = extract_message_details(json_data_list)

    # 断言
    assert actual_result == expected_result, f"预期结果 {expected_result} 与实际结果 {actual_result} 不匹配！"


# 辅助测试：迈入异常情况测试
def test_extract_message_details_with_invalid_data():
    # 非法数据输入
    invalid_data_list = [
        # 消息完全为空
        {},
        # 缺少 "sender" 字段
        {
            'message': [{'type': 'text', 'data': {'text': '11'}}]
        }
    ]

    # 预期输出 (解析后无有效结果)
    expected_result = [
        {
            "sender_id": "未知ID",
            "sender_name": "未知名称",
            "messages": ["11"]
        }
    ]

    # 调用被测函数
    actual_result = extract_message_details(invalid_data_list)

    # 断言
    assert actual_result == expected_result, f"预期结果 {expected_result} 与实际结果 {actual_result} 不匹配！"