'''
875. Koko Eating Bananas
Medium

Topics
Companies
Koko loves to eat bananas. There are n piles of bananas, the ith pile has
piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses
some pile of bananas and eats k bananas from that pile. If the pile has less
than k bananas, she eats all of them instead and will not eat any more bananas
during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas
before the guards return.

Return the minimum integer k such that she can eat all the bananas within h
hours.
 

Example 1:
Input: piles = [3,6,7,11], h = 8
Output: 4

Example 2:
Input: piles = [30,11,23,4,20], h = 5
Output: 30

Example 3:
Input: piles = [30,11,23,4,20], h = 6
Output: 23
 

Constraints:
1 <= piles.length <= 104
piles.length <= h <= 109
1 <= piles[i] <= 109
'''
import math


class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        # min_sum = 0
        # for k in range(1, h, 1):
        #     sum = 0
        #     for pile in piles:
        #         print('pile = ', pile)
        #         time = math.ceil(pile/k)
        #         print('time = ', time)
        #         sum = sum + time
        #     if k == 1:
        #         min_sum = sum
        #     else:
        #         if sum <= h:
        #             min_sum = min(min_sum, sum) 
        #     print('sum = ', sum)
        #     print('min_sum = ', min_sum)
        # return min_sum
        
        # def canEatAllBananas(speed):
        #     total_hours = 0
        #     for pile in piles:
        #         # total_hours += (pile + speed - 1) // speed  # This is equivalent to ceil(pile / speed)
        #         total_hours += math.ceil(pile/speed)
        #     return total_hours <= h

        # left, right = 1, max(piles)
        # print('right = ', right)
        # while left < right:
        #     mid = (left + right) // 2
        #     if canEatAllBananas(mid):
        #         right = mid  # Try a smaller speed
        #     else:
        #         left = mid + 1  # Increase the speed
        # return left
        left, right = 1, max(piles)
        min_hours = right
        while left <= right:
            k = (left + right) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/k)
            if hours <= h:
                min_hours = min(min_hours, k)
                right = k - 1
            else:
                left = k + 1
        return min_hours    

my_solution = Solution()
# Example usage
piles = [3, 6, 7, 11]
h = 8
print(my_solution.minEatingSpeed(piles, h))  # Output: 4

piles = [30,11,23,4,20]
h = 5
print(my_solution.minEatingSpeed(piles, h))  # Output: 30

piles = [30,11,23,4,20]
h = 6
print(my_solution.minEatingSpeed(piles, h))  # Output: 23