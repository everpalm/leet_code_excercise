'''
1899. Merge Triplets to Form Target Triplet
Medium

Topics
Companies

Hint
A triplet is an array of three integers. You are given a 2D integer array
triplets, where triplets[i] = [ai, bi, ci] describes the ith triplet. You are
also given an integer array target = [x, y, z] that describes the triplet you
want to obtain.

To obtain target, you may apply the following operation on triplets any number
of times (possibly zero):

Choose two indices (0-indexed) i and j (i != j) and update triplets[j] to
become [max(ai, aj), max(bi, bj), max(ci, cj)].
For example, if triplets[i] = [2, 5, 3] and triplets[j] = [1, 7, 5],
triplets[j] will be updated to [max(2, 1), max(5, 7), max(3, 5)] = [2, 7, 5].
Return true if it is possible to obtain the target triplet [x, y, z] as an
element of triplets, or false otherwise.

 
Example 1:
Input: triplets = [[2,5,3],[1,8,4],[1,7,5]], target = [2,7,5]
Output: true
Explanation: Perform the following operations:
- Choose the first and last triplets [[2,5,3],[1,8,4],[1,7,5]]. Update the
last triplet to be [max(2,1), max(5,7), max(3,5)] = [2,7,5]. triplets =
[[2,5,3],[1,8,4],[2,7,5]]
The target triplet [2,7,5] is now an element of triplets.

Example 2:
Input: triplets = [[3,4,5],[4,5,6]], target = [3,2,5]
Output: false
Explanation: It is impossible to have [3,2,5] as an element because there is
no 2 in any of the triplets.

Example 3:
Input: triplets = [[2,5,3],[2,3,4],[1,2,5],[5,2,3]], target = [5,5,5]
Output: true
Explanation: Perform the following operations:
- Choose the first and third triplets [[2,5,3],[2,3,4],[1,2,5],[5,2,3]].
Update the third triplet to be [max(2,1), max(5,2), max(3,5)] = [2,5,5].
triplets = [[2,5,3],[2,3,4],[2,5,5],[5,2,3]].
- Choose the third and fourth triplets [[2,5,3],[2,3,4],[2,5,5],[5,2,3]].
Update the fourth triplet to be [max(2,5), max(5,2), max(5,3)] = [5,5,5].
triplets = [[2,5,3],[2,3,4],[2,5,5],[5,5,5]].
The target triplet [5,5,5] is now an element of triplets.
 
Constraints:
1 <= triplets.length <= 105
triplets[i].length == target.length == 3
1 <= ai, bi, ci, x, y, z <= 1000
'''
from typing import List


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x, y, z = target
        found_x, found_y, found_z = False, False, False
    
        for triplet in triplets:
            a, b, c = triplet
            if a <= x and b <= y and c <= z:
                if a == x:
                    found_x = True
                if b == y:
                    found_y = True
                if c == z:
                    found_z = True
        
        return found_x and found_y and found_z
        # temp0 = triplets[0][0]
        # temp1 = triplets[0][1]
        # temp2 = triplets[0][2] 
        # for i in range (1, len(triplets)):
        # # check if Max(triplets[0] = target[0])
        #     temp0 = max(temp0, triplets[i][0])
        #     temp1 = max(temp1, triplets[i][1])
        #     temp2 = max(temp2, triplets[i][2])
        #     if [temp0, temp1, temp2] == target:
        #         return True
        # return False 


sol = Solution()
triplets = [[2,5,3],[1,8,4],[1,7,5]]
target = [2,7,5]
print('Result1 = ', sol.mergeTriplets(triplets,target))

triplets = [[3,4,5],[4,5,6]]
target = [3,2,5]
print('Result2 = ', sol.mergeTriplets(triplets,target))

triplets = [[2,5,3],[2,3,4],[1,2,5],[5,2,3]]
arget = [5,5,5]
print('Result3 = ', sol.mergeTriplets(triplets,target))