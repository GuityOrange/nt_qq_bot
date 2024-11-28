from asyncio import create_task

import uvicorn
from fastapi import FastAPI, Request
from utils.json_utils import extract_message_details
from processors.keyword_trigger import keyword_test_trigger
from processors.history_trigger import history_trigger

app = FastAPI()


@app.post("/")
async def root(request: Request):
    json_data = await request.json()  # 获取事件数据
    msg_data = extract_message_details(json_data)

    # trigger
    create_task(keyword_test_trigger(msg_data))
    create_task(history_trigger(msg_data))


    print(json_data)
    return {}

if __name__ == "__main__":
    uvicorn.run(app, port=8080)