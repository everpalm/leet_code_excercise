'''2. Add Two Numbers
Medium

Topics
Companies
You are given two non-empty linked lists representing two non-negative
integers. The digits are stored in reverse order, and each of their nodes
contains a single digit. Add the two numbers and return the sum as a linked
list.

You may assume the two numbers do not contain any leading zero, except the
number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading
zeros.
'''
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self,
                      l1: Optional[ListNode],
                      l2: Optional[ListNode]) -> Optional[ListNode]:
        # Reverse order
        # prev1 = prev2 = None
        # curr1 = l1
        # curr2 = l2
        # while curr1:
        #     temp1 = curr1.next
        #     curr1.next = prev1
        #     prev1 = curr1
        #     curr1 = temp1

        # while curr2:
        #     temp2 = curr2.next
        #     curr2.next = prev2 
        #     prev2 = curr2
        #     curr2 = temp2
        #     print('curr2 = ', curr2)
    
        # while prev1 and prev2:
        #     sum = prev1.val + prev2.val
        #     prev1 = prev1.next
        #     prev2 = prev2.next
                
        # Get value and sum up
        dummy = ListNode()
        current = dummy
        carry = 0
        
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate the sum and update the carry
            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            
            # Move to the next elements
            current = current.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        return dummy.next

    # Helper function to create linked list from a list
    def create_linked_list(self, lst):
        dummy = ListNode()
        current = dummy
        for num in lst:
            current.next = ListNode(num)
            current = current.next
        return dummy.next

    # Helper function to convert linked list to a list
    def linked_list_to_list(self, node):
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result

# Test the implementation
my_solution = Solution()
l1 = [2, 4, 3]
l2 = [5, 6, 4]
linked_l1 = my_solution.create_linked_list(l1)
linked_l2 = my_solution.create_linked_list(l2)
result = my_solution.addTwoNumbers(linked_l1, linked_l2)
result_list = my_solution.linked_list_to_list(result)
print(result_list)  # Output: [7, 0, 8]
