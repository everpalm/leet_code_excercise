'''
621. Task Scheduler
Medium

Topics
Companies

Hint
You are given an array of CPU tasks, each represented by letters A to Z, and a
cooling time, n. Each cycle or interval allows the completion of one task.
Tasks can be completed in any order, but there's a constraint: identical tasks
must be separated by at least n intervals due to cooling time.

​Return the minimum number of intervals required to complete all tasks.

Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A ->
B.
After completing task A, you must wait two cycles before doing A again. The
same applies to task B. In the 3rd interval, neither A nor B can be done, so
you idle. By the 4th cycle, you can do A again as 2 intervals have passed.

Example 2:
Input: tasks = ["A","C","A","B","D","B"], n = 1
Output: 6
Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.
With a cooling interval of 1, you can repeat a task after just one other task.

Example 3:
Input: tasks = ["A","A","A", "B","B","B"], n = 3
Output: 10
Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle
-> idle -> A -> B.
There are only two types of tasks, A and B, which need to be separated by 3
intervals. This leads to idling twice between repetitions of these tasks.

Constraints:
1 <= tasks.length <= 104
tasks[i] is an uppercase English letter.
0 <= n <= 100
'''
from collections import Counter
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Step 1: Count the frequency of each task
        task_counts = Counter(tasks)
        # print(f'task_counts = {task_counts}')
        # print(f'task_counts.values() = {task_counts.values()}')

        # Step 2: Find the maximum frequency
        max_freq = max(task_counts.values())
        # print(f'max_freq = {max_freq}')
        
        # Step 3: Find the number of tasks that have the maximum frequency
        # temp = list(task_counts.values())

        # print(f'list(task_counts.values()) = {temp}')
        # print(f'list(task_counts.values()).count(max_freq) = {temp.count(max_freq)}')
        max_freq_tasks = list(task_counts.values()).count(max_freq)
        
        # Step 4: Calculate the frame length required to arrange the most frequent tasks
        frame_length = (max_freq - 1) * (n + 1) + max_freq_tasks
        
        # Step 5: The minimum length of intervals needed is the maximum between frame length and total number of tasks
        return max(frame_length, len(tasks))
    


solution = Solution()
# print('Result1 = ', solution.leastInterval(["A","A","A","B","B","B"], 2))  # Output: 8
print('Result2 = ', solution.leastInterval(["A","C","A","B","D","B"], 1))  # Output: 6
# print('Result3 = ', solution.leastInterval(["A","A","A", "B","B","B"], 3))  # Output: 10