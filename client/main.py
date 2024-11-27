import uvicorn
from fastapi import FastAPI, Request
from utils.json_utils import extract_message_details
from processors.keyword_trigger import event_kw_hello_world

app = FastAPI()


@app.post("/")
async def root(request: Request):
    json_data = await request.json()  # 获取事件数据
    data = extract_message_details(json_data)
    event_kw_hello_world(data)
    print(json_data)
    return {}

if __name__ == "__main__":
    uvicorn.run(app, port=8080)