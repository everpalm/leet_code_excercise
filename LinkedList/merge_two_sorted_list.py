class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    # Initialize a dummy node and a current pointer pointing to it
    dummy = ListNode()
    current = dummy
    
    # Iterate through both lists until one is exhausted
    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next 
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
        
    # Attach any remaining elements of list1 or list2
    if list1:
        current.next = list1
    elif list2:
        current.next = list2
        
    # The head of the merged list is next to the dummy node
    return dummy.next

# Note: The function calls are commented out to adhere to the instructions.
# Example usage (uncomment in a real environment):
# list1 = ListNode(1, ListNode(2, ListNode(4)))
# list2 = ListNode(1, ListNode(3, ListNode(4)))
# merged_list_head = mergeTwoLists(list1, list2)
# while merged_list_head:
#     print(merged_list_head.val)
#     merged_list_head = merged_list_head.next
