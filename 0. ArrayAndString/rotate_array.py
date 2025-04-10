'''
給定一個整數陣列 nums 和一個非負整數 k, 請將陣列向右旋轉 k 個位置，要求時間複雜度為 O(n) 且在空間上使用原地演算法(in-place)。
輸入: nums = [1,2,3,4,5,6,7], k = 3  
輸出: [5,6,7,1,2,3,4]
'''
from typing import List

class Solution():
    def rotate_array(self, nums: List[int], k: int) -> List:
        n = len(nums)
        k %= n
        nums.reverse()
        # nums[:k].reverse()
        nums[:k] = nums[:k][::-1]
        # nums[k + 1:].reverse()
        nums[k:] = nums[k:][::-1]
        return nums
    
    def inplace_operation(self, nums: List[int], k: int) -> List:
        n = len(nums)
        k %= n  # 處理 k 大於 n 的情況
        # 依序反轉整個串列、前 k 個元素，再反轉剩下的部分
        def reverse(ints: List[int], start: int, end: int) -> None:
            while start < end:
                ints[start], ints[end] = ints[end], ints[start]
                start += 1
                end -= 1
                # print("ints = ", ints)

        reverse(nums, 0, n - 1)
        # print('nums = ', nums)
        reverse(nums, 0, k - 1)
        # print('nums = ', nums)
        reverse(nums, k, n - 1)
        # print('nums = ', nums)
        return nums

solution = Solution()
a = [1, 2, 3, 4, 5, 6, 7]
print("solution1 = ", solution.rotate_array(a, 3))
b = [1, 2, 3, 4, 5, 6, 7]
print("solution2 = ", solution.inplace_operation(b, 3))
