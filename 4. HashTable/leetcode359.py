import time
import random

class Solution:
    def __init__(self):
        self.last_printed = {}
    
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        # 清理超过10秒的旧消息
        self.cleanup_old_messages(timestamp)

        if message in self.last_printed:
            if timestamp - self.last_printed[message] >= 10:
                self.last_printed[message] = timestamp
                return True
            else:
                return False
        else:
            self.last_printed[message] = timestamp
            return True
    
    def cleanup_old_messages(self, current_timestamp: int):
        # 删除字典中时间戳超过10秒的键
        to_delete = [msg for msg, time in self.last_printed.items() if current_timestamp - time >= 10]
        for msg in to_delete:
            del self.last_printed[msg]

def output_log() -> tuple:
    # 模拟带有时间戳的消息输出
    current_time = int(time.time())
    messages = ["foo", "bar", "baz"]
    message = random.choice(messages)
    return current_time, message

def main():
    solution = Solution()
    
    while True:
        timestamp, message = output_log()
        if solution.shouldPrintMessage(timestamp, message):
            print(f"{timestamp}: {message}")
        
        # 模拟延迟，以避免紧密循环；在实际应用中，消息会以不同的间隔到达
        time.sleep(random.uniform(0.5, 2.0))  # 随机睡眠0.5到2秒

# 运行主函数
main()