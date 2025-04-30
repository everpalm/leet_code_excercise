'''
238. Product of Array Except Self
Medium

Topics
Companies

Hint
Given an integer array nums, return an array answer such that answer[i] is
equal to the product of all the elements of nums except nums[i].
[1, 2, 3] --> [1, 2, 3, 6] --> [6]
[1, 2, 3, 4] --> [1, 2, 3, 4, 6, 8, 12, 24] --> [6, 8 , 12, 24]

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
integer.

You must write an algorithm that runs in O(n) time and without using the
division operation.

 
Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]


Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Note:
 1  [1] [2] [3]
[0]  1  [2] [3]
[0] [1]  1  [3]
[0] [1] [2]  1
^^^^^^^^^^ start out with the left side
answer[0] = 1
answer[1] = answer[0] * num[0] = 1 * 1
answer[2] = answer[1] * num[1] = 1 * 2
answer[3] = answer[2] * num[2] = 2 * 3
'''
# import operator
from typing import List


class Solution(object):
    def brute_force(self, nums):
        n = len(nums)
        output = []

        for i in range(n):
            prod = 1
            for j in range(n):
                if i != j:
                    prod *= nums[j]
            output.append(prod)

        return output
    
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        # The answer array to be returned
        answer = [1] * length
        # print('answer = ', answer)
        # answer[i] contains the product of all the elements to the left
        # For the element at index 0, there are no elements to the left, so answer[0] should be 1
        # answer[0] = 1
        for i in range(1, length):
            answer[i] = nums[i - 1] * answer[i - 1]
            print(f'answer[{i}] = ', answer[i])
        # print('answer = ', operator.mul(nums))
        # R is a running product of elements to the right
        multiplier = 1
        for j in reversed(range(length)):
            # For the index 'i', R would contain the product of all elements to the right.
            # We update R accordingly
            # print('j = ', j)
            answer[j] = answer[j] * multiplier
            print(f'R answer[{j}] = ', answer[j])
            multiplier *= nums[j]
            # print(f'multiplier = ', multiplier)
        return answer

    def productExceptSelf1(self, nums: List[int]) -> List:
        n = len(nums)
        answer = [0] * n
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for j in range(n - 1, -1, -1):
            answer[j] *= suffix
            suffix *= nums[j]

        return answer  

my_solution = Solution()
nums = [1, 2, 3, 4]
result = my_solution.productExceptSelf(nums)
print('Test1 result = ', result)
result = my_solution.brute_force(nums)
print('Test1-1 result = ', result)
result = my_solution.productExceptSelf1(nums)
print('Test1-2 result = ', result)

my_solution = Solution()
nums = [-1, -1, 0, -3, -3]
result = my_solution.productExceptSelf(nums)
print('Test2 result = ', result)
result = my_solution.brute_force(nums)
print('Test2-1 result = ', result)
result = my_solution.productExceptSelf1(nums)
print('Test2-2 result = ', result)
'''
我們以數組 `[1, 2, 3, 4]` 為例，詳細列出計算過程，分別計算左側乘積和右側乘積，最後合併得出結果。

---

### 第一步：計算左側乘積

我們建立一個與原數組等長的 `answer` 陣列，初始值都為 1。這個陣列在第一遍遍歷中存放每個位置左邊所有數的乘積。

- **初始設定：**  
  `answer[0] = 1` （因為最左側沒有數字）

- **計算過程：**
  - **i = 1**  
    `answer[1] = answer[0] * nums[0] = 1 * 1 = 1`
  - **i = 2**  
    `answer[2] = answer[1] * nums[1] = 1 * 2 = 2`
  - **i = 3**  
    `answer[3] = answer[2] * nums[2] = 2 * 3 = 6`

- **左側乘積結果：**  
  此時 `answer = [1, 1, 2, 6]`

---

### 第二步：計算右側乘積並合併

接下來，我們用一個變數 `right` 表示當前右側所有數的乘積，初始設為 1。從右側開始遍歷, 將 `right` 與對應的 `answer` 元素相乘，
然後更新 `right`。

- **初始設定：**  
  `right = 1` （最右側無數）

- **計算過程：**
  - **i = 3(最右邊)**  
    - 更新 `answer[3] = answer[3] * right = 6 * 1 = 6`  
    - 更新 `right = right * nums[3] = 1 * 4 = 4`
  - **i = 2**  
    - 更新 `answer[2] = answer[2] * right = 2 * 4 = 8`  
    - 更新 `right = right * nums[2] = 4 * 3 = 12`
  - **i = 1**  
    - 更新 `answer[1] = answer[1] * right = 1 * 12 = 12`  
    - 更新 `right = right * nums[1] = 12 * 2 = 24`
  - **i = 0(最左邊）：**  
    - 更新 `answer[0] = answer[0] * right = 1 * 24 = 24`  
    - 更新 `right = right * nums[0] = 24 * 1 = 24` （最後一步，`right` 的值更新完畢，但不再使用）

- **右側乘積合併結果：**  
  最終 `answer = [24, 12, 8, 6]`

---

### 總結

1. **左側遍歷結果：** `[1, 1, 2, 6]`  
   （每個位置存放的是該位置左側所有數的乘積）

2. **右側遍歷合併：**  
   依次從右邊將右側乘積合併到 `answer` 中，得到最終結果 `[24, 12, 8, 6]`
'''