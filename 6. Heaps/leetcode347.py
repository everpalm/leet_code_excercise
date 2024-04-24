'''
347. Top K Frequent Elements
Solved
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
        # freq = Counter(nums)
        # # print('most common = ', freq.most_common(2))
        # top_k = freq.most_common(k)
        # print('top_k = ', top_k)
        # elements = [element[0] for element in top_k]
        # print('elements = ', elements)
        # return elements
        
        # # Build a heap of the top k elements and their frequencies
        # # Use negative frequency for max-heap behavior using min-heap
        freq = Counter(nums)
        print('freq = ', freq)
        heap = []
        for num, count in freq.items():
            heapq.heappush(heap, (count, num))
            print('heap = ', heap)
            if len(heap) > k:
                heapq.heappop(heap)
        
        # Extract the elements from the heap
        top_k = [heapq.heappop(heap)[1] for _ in range(len(heap))]
        print('top_k = ', top_k)
        return top_k[::-1]  # Return in any order

        
my_solution = Solution()
nums = [1,1,1,2,2,3]
k = 2
print(my_solution.topKFrequent(nums, k))  # Output: [1, 2]