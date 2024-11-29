from datetime import datetime

from enetity.data_enetity import MsgData
from enetity.good_morning_enetity import GoodMorningManager
from utils.post_utils import send_text_msg, send_mface_msg, send_at_text_msg
from utils.llm_utils import daily_good_morning_roll
from utils.json_utils import check_equal_key_words

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

good_morning_manager = GoodMorningManager()

async def event_kw_hello_world(data: MsgData) -> None:
    """
    通过关键词触发的事件
    """
    messages = data.messages

    if check_equal_key_words(messages, ['.hello']):
        send_text_msg(data.target_id, data.message_type, "Hello World")


async def event_kw_mface(data: MsgData) -> None:
    """
    通过关键词触发的事件
    """
    messages = data.messages

    if check_equal_key_words(messages, ['.表情包']):
        send_mface_msg(data.target_id, data.message_type, '[哈欠]', 'https://gxh.vip.qq.com/club/item/parcel/item/12/12a2308d790509abb90cafff6161d900/raw300.gif', '12a2308d790509abb90cafff6161d900', 240792, '0dc7681880e867fc')


async def event_kw_good_morning(data: MsgData) -> None:
    """
    早安事件，每人每日只可以触发一次，且只能在指定时间段触发
    """
    messages = data.messages

    current_time = datetime.now()

    # 获取当前小时
    current_hour = current_time.hour

    # 判断时间区间
    if check_equal_key_words(messages, ['早上好', '早安', '早', 'morning', 'good morning']):
        if 0 <= current_hour < 14:
            if good_morning_manager.update(data.message_type, data.target_id, data.sender_id):
                lucy_msg = daily_good_morning_roll()
                send_text_msg(data.target_id, data.message_type, f"{data.sender_name}\n{lucy_msg}",forward_msg_flag=True)
            else:
                send_at_text_msg(data.target_id, data.message_type, "(*´∀`)~♥今天已经早安过了哦", data.sender_id)
        elif 14 <= current_hour < 19:
            send_at_text_msg(data.target_id, data.message_type, "Σ(ﾟДﾟ；≡；ﾟдﾟ)现在是下午了，早上好是什么意思？", data.sender_id)
        elif 19 <= current_hour < 24:
            send_at_text_msg(data.target_id, data.message_type, "(*´･д･)?现在是晚上了，早上好是什么意思？", data.sender_id)
        else:
            print("时间不正确")  # 理论上不会进入此分支

