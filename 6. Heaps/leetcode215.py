'''
215. Kth Largest Element in an Array
Medium

Topics
Companies
Given an integer array nums and an integer k, return the kth largest element
in the array.

Note that it is the kth largest element in the sorted order, not the kth
distinct element.

Can you solve it without sorting?

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 
Constraints:
1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104
'''
from typing import List
import heapq

class Solution():
    def findKthLargest(self, nums, k):
        # Create a min-heap with the first k elements of the array
        min_heap = nums[:k]
        heapq.heapify(min_heap)
        
        # Process the remaining elements
        for num in nums[k:]:
            # It's more efficient to compare new element to min_heap[0]
            # and use heapreplace instead of heappushpop
            if num > min_heap[0]: 
                # Only consider elements greater than the
                #smallest element in the heap
                heapq.heapreplace(min_heap, num)
        
        # The root of the heap is the kth largest element
        return min_heap[0]
        # min_heap = [num for num in nums]
        # min_heap = nums[:]
        # heapq.heapify(min_heap)
        # for i in range(len(min_heap) - k):
        #     heapq.heappop(min_heap)
        # return min_heap[0]

# 註解及建議
# 效率:
# 這個方法需要建立一個大小為 n 的堆，然後進行 n-k 次 heappop 操作。總體時間複雜度是 O(n + (n-k) log n)。
# 上一個被註釋掉的方法，只需要建立一個大小為 k 的堆，並且在插入新的元素時保持堆的大小不變，時間複雜度是 O(k + (n-k) log k)，對於較大的 k 更加高效。
#
# 內存使用：

# 你的新方法需要在內存中保持整個數組的堆，而之前的方法只需要保持大小為 k 的堆，因此之前的方法對於內存使用也更有效。
        
solution = Solution()
# Example usage
# nums1 = [3, 2, 1, 5, 6, 4]
# k1 = 2
# print('Result1 = ', solution.findKthLargest(nums1, k1))  # Output: 5

# nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
# k2 = 4
# print('Result2 = ', solution.findKthLargest(nums2, k2))  # Output: 4

nums3 = [1, 2, 3]
k3 = 2
print('Result2 = ', solution.findKthLargest(nums3, k3))  # Output: 4
