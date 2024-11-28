"""
俺也一样！！
"""
from enetity.data_enetity import MsgData
from enetity.history_enetity import HistoryManager
from utils.post_utils import send_text_msg

"""
通过关键词来触发的事件
data:
target_id: 目标ID
sender_id: 发送者ID
sender_name: 发送者名称
messages: 消息列表
datas: 详细的消息列表
message_type: 消息类型
group_id: 群聊ID (可选)
"""

async def event_for_text_one_plus(msg_data: MsgData, history_manager: HistoryManager) -> None:
    """
    当出现3次同样的文本消息时，触发事件
    """

    records_datas_deque = history_manager.get(msg_data.message_type, msg_data.target_id)

    # 取最后3条消息
    newest_datas_list = list(records_datas_deque)[-3:]
    if len(newest_datas_list) != 3:
        return

    # 检查是否都长度为1, 且类型为text, 且内容相同
    text_list = []
    for datas in newest_datas_list:
        if len(datas) != 1:
            return
        data = datas[0]
        if data['type'] != 'text':
            return
        text_list.append(data['data']['text'])
    if len(set(text_list)) == 1:
        # 触发事件
        send_text_msg(msg_data.target_id, msg_data.message_type, text_list[0])
        history_manager.delete(msg_data.message_type, msg_data.target_id)




