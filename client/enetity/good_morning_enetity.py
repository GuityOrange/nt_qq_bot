from threading import Lock
import datetime

class GoodMorningManager:
    def __init__(self):
        self.history = set()
        self.date = None
        # 添加线程锁以确保线程安全
        self.lock = Lock()

    def update(self, record_type: str, record_id: int, sender_id: int) -> bool:
        """
        更新指定类型和 ID 下的记录。
        如果记录不存在，返回 True；否则返回 False。
        """
        today_date = datetime.date.today()
        key = (record_type, record_id, sender_id)
        with self.lock:  # 使用锁保护共享数据操作
            if self.date != today_date:
                self.history = set()
                self.date = today_date
            if key not in self.history:
                self.history.add(key)
                return True
            return False

