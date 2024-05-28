'''
206. Reverse Linked List
Solved
Easy

Topics
Companies
Given the head of a singly linked list, reverse the list, and return the
reversed list.

Example 1:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:

Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
 
Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
 

Follow up: A linked list can be reversed either iteratively or recursively.
Could you implement both?'''
from typing import List
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    def list_to_linkedlist(self, arr):
        if not arr:
            return None
        head = ListNode(arr[0])
        current = head
        for value in arr[1:]:
            current.next = ListNode(value)
            current = current.next
        return head

    def linkedlist_to_list(self, head):
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result


my_solution = Solution()
head = [1, 2, 3, 4, 5]
linked_head = my_solution.list_to_linkedlist(head)
reversed_head = my_solution.reverseList(linked_head)
reversed_list = my_solution.linkedlist_to_list(reversed_head)
print('Result1 = ', reversed_list)
# print('Result1 = ', my_solution.reverseList(reversed_head))

head = [1, 2]
linked_head = my_solution.list_to_linkedlist(head)
reversed_head = my_solution.reverseList(linked_head)
reversed_list = my_solution.linkedlist_to_list(reversed_head)
print('Result2 = ', reversed_list)

head = []
linked_head = my_solution.list_to_linkedlist(head)
reversed_head = my_solution.reverseList(linked_head)
reversed_list = my_solution.linkedlist_to_list(reversed_head)
print('Result3 = ', reversed_list)