from collections import deque
from threading import Lock

class HistoryManager:
    def __init__(self):
        # 使用字典保存历史记录，字典的 key 是 (type, id) 元组，value 是一个队列
        self.history = {}
        # 添加线程锁以确保线程安全
        self.lock = Lock()

    def update(self, record_type, record_id, new_record):
        """
        更新指定类型和 ID 下的记录。
        记录保存在一个队列中，最多保留 5 条记录。
        如果超过 5 条，自动删除最早的记录。
        """
        key = (record_type, record_id)
        with self.lock:  # 使用锁保护共享数据操作
            if key not in self.history:
                self.history[key] = deque(maxlen=5)  # 限制队列最大长度为 5
            self.history[key].append(new_record)

    def delete(self, record_type, record_id):
        """
        删除指定类型和 ID 的记录。
        """
        key = (record_type, record_id)
        with self.lock:  # 使用锁保护共享数据操作
            if key in self.history:
                del self.history[key]

    def get(self, record_type, record_id):
        """
        获取指定类型和 ID 下所有的记录。
        如果不存在，返回空列表。
        """
        key = (record_type, record_id)
        with self.lock:  # 使用锁保护读取操作
            # 返回队列的副本以避免外部修改原始队列
            return list(self.history.get(key, []))