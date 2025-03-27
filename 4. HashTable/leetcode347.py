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
# import heapq
from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # my_hash = {}
        # count = 0
        # for num in nums:
        #     count = my_hash.get(num, 0)
        #     my_hash[num] = count + 1
        # print('my_hash = ', my_hash)

        my_hash = Counter(nums)
        output = []
        for key, value in my_hash.items():
            # if value >= k:
        #         output.append(key)
        # output = sorted(my_hash.items(), key=lambda item: item[1], reverse=True)
        # return [num for num, _ in output[:k]]
            output.append((value, key))
        output.sort(reverse=True)
        return [key for _, key in output[:k]]
        # count = Counter(nums)
    
        # Create a min-heap for the top k frequent elements
        # Using negative frequency to simulate a max-heap using a min-heap
        # heap = []
        # for num, freq in count.items():
        #     heapq.heappush(heap, (-freq, num))
        #     if len(heap) > k:
        #         heapq.heappop(heap)
        
        # # Extract the elements from the heap
        # top_k = [heapq.heappop(heap)[1] for _ in range(len(heap))]
        # return top_k[::-1] 

my_solution = Solution()
nums = [1, 1, 1, 2, 2, 3]
k = 2
print('result1 = ', my_solution.topKFrequent(nums, k))

nums = [1]
k = 1
print('result2 = ', my_solution.topKFrequent(nums, k))