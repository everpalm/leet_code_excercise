'''
19. Remove Nth Node From End of List
Solved
Medium

Topics
Companies

Hint
Given the head of a linked list, remove the nth node from the end of the list
and return its head.

 
Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
 

Follow up: Could you do this in one pass?
'''
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = right = dummy
        for _ in range(n + 1):
            right = right.next

        while right:
            right = right.next
            left = left.next
        
        left.next = left.next.next
        return dummy.next
    
    # Code for testing purposes
    def printList(self, head: ListNode) -> None:
        while head:
            print(head.val, end=" -> ")
            head = head.next
        print("None")

    def list_to_linkedlist(self, lst):
        dummy = ListNode()
        current = dummy
        for value in lst:
            current.next = ListNode(value)
            current = current.next
        return dummy.next


my_solution = Solution()
head = [1,2,3,4,5]
n = 2
linked_list = my_solution.list_to_linkedlist(head)
result_list = my_solution.removeNthFromEnd(linked_list, n)
my_solution.printList(result_list)

head = [1]
n = 1
linked_list = my_solution.list_to_linkedlist(head)
result_list = my_solution.removeNthFromEnd(linked_list, n)
my_solution.printList(result_list)

head = [1,2]
n = 1
linked_list = my_solution.list_to_linkedlist(head)
result_list = my_solution.removeNthFromEnd(linked_list, n)
my_solution.printList(result_list)
        
        
