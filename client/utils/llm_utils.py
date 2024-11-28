import random
import time

from openai import OpenAI

from config.config_private import DEEP_SEEK_API

def post_to_llm(prompt: str):
    """
    与大模型进行一次无上下文交互。

    Args:
        prompt (str): 用户输入的 prompt 信息。

    Returns:
        str: 模型返回的响应内容。
    """
    # 初始化 OpenAI 客户端
    client = OpenAI(api_key=DEEP_SEEK_API, base_url="https://api.deepseek.com")

    # 请求交互
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": prompt},
        ],
        stream=False
    )

    # 返回模型响应
    return response.choices[0].message.content


def daily_good_morning_roll() -> str:
    # 获取3个0-100的随机int
    random.seed(time.time())
    roll = [random.randint(0, 100) for _ in range(3)]
    final_prompt = (f"请根据下面的三个数据编一个简短的小故事，这个小故事的人称是“你”，故事的内容是符合下面三个运气数值的日常，"
           f"解释："
           f"1.财运是和钱相关的运气，桃花运是和爱情或者艳遇相关的运气，幸运是和其他运气相关的运气。"
           f"2.其中1-10是非常差，11-30是差，31-60是一般，61-90是好，91-100是特别好，"
           f"3.如果数值是一般的话，就不用在故事中体现。"
           f"要求："
           f"1.故事要简短，不超过100字。"
           f"2.故事要符合三个数值的含义。"
           f"3.故事要有戏剧性，要很有趣。"
           f"————————"
           f"例子1："
           f"数值：今日财运：99、今日桃花运：33、今日幸运：8。"
           f"回复：今天你在街上捡到了一百块钱，最后你还中了彩票！可惜运气实在太差了，钱和彩票都被一阵风吹走了。"
           f"————————"
           f"例子2："
           f"数值：今日财运：33、今日桃花运：79、今日幸运：99。"
           f"回复：今天你遇见了一个H罩杯的大姐姐，你帮她指了路，她和你加了微信，回家的路上有一棵树倒了，刚好没砸到你，原来是那个大姐姐帮你把倒下的树撑住了，运气简直好的不行！"
           f"————————"
           f"你需要编造故事的数据如下:"
           f"数据：今日财运：{roll[0]}、今日桃花运{roll[1]}、今日幸运{roll[2]}。"
           f"回复："
                    )

    msg = post_to_llm(final_prompt)
    final_content = f"\n(≧∀≦)ゞ早上好~查看你今天的运气如何：\n今日财运: {roll[0]}\n今日桃花运: {roll[1]}\n今日幸运: {roll[2]}\n猜测一下你的一天：\n{msg}"
    return final_content