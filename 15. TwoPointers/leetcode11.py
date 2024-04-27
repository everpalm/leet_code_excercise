'''
11. Container With Most Water
Medium

Topics
Companies

Hint
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
 

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
'''
class Solution:
    def maxArea(self, height: list) -> int:
        max_area = area = 0
        n = len(height)
        left, right = 0, n-1
        # for i in range(n):
        #     right = n-1
        #     print(f'height[{i}] = {height[i]}')
            # while i < right:
            #     print(f'height[{right}] = {height[right]}')
            #     area = min(height[i], height[right]) * abs(i - right)
            #     print(f'area = {area}')
            #     max_area = max(max_area, area)
            #     print(f'max_area = {max_area}')
            #     right -= 1
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
        # max_area = 0
        # left, right = 0, len(height) - 1

        # while left < right:
        #     # Calculate the area with the current boundaries
        #     width = right - left
        #     min_height = min(height[left], height[right])
        #     current_area = min_height * width
            
        #     # Update the max_area if the current one is larger
        #     max_area = max(max_area, current_area)
            
        #     # Move the pointer pointing to the shorter line towards the center
        #     if height[left] < height[right]:
        #         left += 1
        #     else:
        #         right -= 1

        # return max_area
    

my_solution = Solution()
height = [1,8,6,2,5,4,8,3,7]
print(f'Result1 = {my_solution.maxArea(height)}')

height = [2,1,4]
print(f'Result2 = {my_solution.maxArea(height)}')