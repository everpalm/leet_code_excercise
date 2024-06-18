'''
Design a logger system that receive stream of messages along with its
timestamps, each message should be printed if and only if it is not printed in
the last 10 seconds.

Given a message and a timestamp (in seconds granularity), return true if the
message should be printed in the given timestamp, otherwise returns false.

It is possible that several messages arrive roughly at the same time.
'''
# class Solution:
#     def __init__(self):
#         self.last_printed = {}
    
#     def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
#         if message in self.last_printed:
#             if timestamp - self.last_printed[message] >= 10:
#                 self.last_printed[message] = timestamp
#                 return True
#             else:
#                 return False
#         else:
#             self.last_printed[message] = timestamp
#             return True

# # Example usage
# solution = Solution()
# print(solution.shouldPrintMessage(1, "foo"))  # True
# print(solution.shouldPrintMessage(2, "bar"))  # True
# print(solution.shouldPrintMessage(3, "foo"))  # False
# print(solution.shouldPrintMessage(11, "foo")) # True
# print(solution.shouldPrintMessage(12, "bar")) # True
# print(solution.shouldPrintMessage(13, "bar")) # False

import time
import random

class Solution:
    def __init__(self):
        self.last_printed = {}
    
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.last_printed:
            if timestamp - self.last_printed[message] >= 10:
                self.last_printed[message] = timestamp
                return True
            else:
                return False
        else:
            self.last_printed[message] = timestamp
            return True

def output_log() -> tuple:
    # Simulate the output of messages with timestamps
    current_time = int(time.time())
    # current_time = time.time()
    messages = ["foo", "bar", "baz"]
    message = random.choice(messages)
    return current_time, message

def main():
    solution = Solution()
    start_time = int(time.time())
    
    while True:
        timestamp, message = output_log()
        if solution.shouldPrintMessage(timestamp, message):
            print(f"{timestamp}: {message}")
        
        # Simulate a delay to avoid tight loop; in a real-world scenario, messages would come in at different intervals
        time.sleep(random.uniform(0.5, 2.0))  # Sleep for a random time between 0.5 to 2 seconds

# Run the main function
main()



