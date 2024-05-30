'''
21. Merge Two Sorted Lists
Solved
Easy

Topics
Companies
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing
together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.        
'''
# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize a dummy node and a current pointer pointing to it
        dummy = ListNode()
        new_list = dummy
        while list1 and list2:
            if list1.val < list2.val:
                new_list.next = list1
                list1 = list1.next
            else:
                new_list.next = list2
                list2 = list2.next
            new_list = new_list.next

        if list1:
            new_list.next = list1
        if list2:
            new_list.next = list2
        return dummy.next
    
    def list_to_linkedlist(self, lst):
        dummy = ListNode()
        current = dummy
        for value in lst:
            current.next = ListNode(value)
            current = current.next
        return dummy.next

    def linkedlist_to_list(self, node):
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result
    
my_solution = Solution()
list1 = [1,2,4]
list2 = [1,3,4]

linked_list1 = my_solution.list_to_linkedlist(list1)
linked_list2 = my_solution.list_to_linkedlist(list2)
merged_list = my_solution.mergeTwoLists(linked_list1, linked_list2)
print('Result1 = ', my_solution.linkedlist_to_list(merged_list))

list1 = []
list2 = []

linked_list1 = my_solution.list_to_linkedlist(list1)
linked_list2 = my_solution.list_to_linkedlist(list2)
merged_list = my_solution.mergeTwoLists(linked_list1, linked_list2)
print('Result2 = ', my_solution.linkedlist_to_list(merged_list))


list1 = []
list2 = [0]

linked_list1 = my_solution.list_to_linkedlist(list1)
linked_list2 = my_solution.list_to_linkedlist(list2)
merged_list = my_solution.mergeTwoLists(linked_list1, linked_list2)
print('Result3 = ', my_solution.linkedlist_to_list(merged_list))