'''
347. Top K Frequent Elements
Medium

Topics
Companies
Given an integer array nums and an integer k, return the k most frequent
elements. You may return the answer in any order.

 

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]
 

Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n),
where n is the array's size.
'''
import heapq
from collections import Counter


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = Counter(nums)
        output = []
        for num, freq in count.items():
            output.append((freq, num))
        output.sort(reverse=True)
        return [num for _, num in output[:k]]
    
    def min_heap(self, nums, k):
        # Create a min-heap for the top k frequent elements
        # Using negative frequency to simulate a max-heap using a min-heap
        count = Counter(nums)
        heap = []
        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        # # Extract the elements from the heap
        top_k = [heapq.heappop(heap)[1] for _ in range(len(heap))]
        return top_k[::-1] 
    

my_solution = Solution()
nums = [1, 1, 1, 2, 2, 3]
k = 2
print('result1 = ', my_solution.topKFrequent(nums, k))
print('result1-1 = ', my_solution.min_heap(nums, k))

nums = [1]
k = 1
print('result2 = ', my_solution.topKFrequent(nums, k))
print('result2-1 = ', my_solution.min_heap(nums, k))
