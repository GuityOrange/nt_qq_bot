import random
import time

from utils.llm_utils import post_to_llm

def test_post_to_llm():
    msg = post_to_llm("Hello, world!")
    print(msg)
    assert len(msg) > 0


