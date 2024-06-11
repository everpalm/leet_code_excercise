'''
138. Copy List with Random Pointer
Medium

Topics
Companies

Hint
A linked list of length n is given such that each node contains an additional
random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n
brand new nodes, where each new node has its value set to the value of its
corresponding original node. Both the next and random pointer of the new nodes
should point to new nodes in the copied list such that the pointers in the
original list and copied list represent the same list state. None of the
pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where
X.random --> Y, then for the corresponding two nodes x and y in the copied
list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each
node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random
pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.

 
Example 1:
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

Example 2:
Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]

Example 3:
Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
 

Constraints:

0 <= n <= 1000
-104 <= Node.val <= 104
Node.random is null or is pointing to some node in the linked list.
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # Step 1: Create new nodes and insert them into the original list
        curr = head
        while curr:
            new_node = Node(curr.val, curr.next)
            curr.next = new_node
            curr = new_node.next

        # Step 2: Copy the random pointers
        curr = head
        while curr:
            if curr.random:
                # print('curr.val = ', curr.val)
                # print('curr.random.val = ', curr.random.val)
                # print('curr.random.next.val = ', curr.random.next.val)
                curr.next.random = curr.random.next
            curr = curr.next.next

        # Step 3: Separate the copied list from the original list
        curr = head # Current pointer: Start out from head
        new_head = curr.next # New head: Memorize new head 
        while curr: # As long as curr is not None
            copy = curr.next # Update copy node with next node of curr
            curr.next = copy.next # Recover original linked list
            if copy.next:
                copy.next = copy.next.next
            curr = curr.next
        return new_head
    
    # Code for testing purposes
    def printList(self, head: Node) -> None:
        curr = head
        output = []
        while curr:
            random_index = None
            if curr.random:
                # Find the index of the random node
                index = head
                count = 0
                while index is not None:
                    if index == curr.random:
                        random_index = count
                        break
                    index = index.next
                    count += 1
            output.append(f"[{curr.val}, {random_index}]")
            curr = curr.next
        print(" -> ".join(output))

    def list_to_linkedlist(self, lst):
        if not lst:
            return None
        
        nodes = [Node(val[0]) for val in lst]
        for i in range(len(nodes)-1):
            nodes[i].next = nodes[i+1]

        for i, val in enumerate(lst):
            if val[1] is not None:
                nodes[i].random = nodes[val[1]]
        return nodes[0]

my_solution = Solution()

head = [[7,None],[13,0],[11,4],[10,2],[1,0]]
linked_list = my_solution.list_to_linkedlist(head)
my_solution.printList(my_solution.copyRandomList(linked_list))

head = [[1,1],[2,1]]
linked_list = my_solution.list_to_linkedlist(head)
my_solution.printList(my_solution.copyRandomList(linked_list))

head = [[3,None],[3,0],[3,None]]
linked_list = my_solution.list_to_linkedlist(head)
my_solution.printList(my_solution.copyRandomList(linked_list))