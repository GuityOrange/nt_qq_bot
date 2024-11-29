from utils.llm_utils import post_to_llm, daily_good_morning_roll

def test_post_to_llm():
    msg = post_to_llm("Hello, world!")
    print(msg)
    assert len(msg) > 0


def test_daily_good_morning_roll():
    print(daily_good_morning_roll())
