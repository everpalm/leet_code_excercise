'''
143. Reorder List
Medium

Topics
Companies
You are given the head of a singly linked-list. The list can be represented
as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may
be changed.

 
Example 1:
Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
 

Constraints:

The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # fast = slow = head
        # dummy = ListNode()
        # new_list = dummy
        # while fast.next and fast.next.next:
        #     fast = fast.next.next
        #     print('fast = ', fast)
        #     slow = slow.next
        # prev, curr = None, slow
        # while curr:
        #     temp = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = temp
        # while curr and slow:
        #     if curr.value > slow.value:
        #         new_list.next = slow
        #         slow = slow.next
        #     else:
        #         new_list.next = curr
        #         curr = curr.next
        # if curr:
        #     new_list.next = curr
        # if slow:
        #     new_list.next = slow
        # return dummy.next
        if not head or not head.next:
            return
    
        # Step 1: Find the middle of the list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse the second half of the list
        prev, curr = None, slow
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        
        # Step 3: Merge the two halves
        first, second = head, prev
        while second.next:
            first_next = first.next
            second_next = second.next
            
            first.next = second
            second.next = first_next
            
            first = first_next
            second = second_next

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
head = [1,2,3,4]
linked_list = my_solution.list_to_linkedlist(head)
my_solution.reorderList(linked_list)
my_solution.printList(linked_list)

head = [1,2,3,4,5]
linked_list = my_solution.list_to_linkedlist(head)
my_solution.reorderList(linked_list)
my_solution.printList(linked_list) 

head = [1]
linked_list = my_solution.list_to_linkedlist(head)
my_solution.reorderList(linked_list)
my_solution.printList(linked_list) 

head = []
linked_list = my_solution.list_to_linkedlist(head)
my_solution.reorderList(linked_list)
my_solution.printList(linked_list) 