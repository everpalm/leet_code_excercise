class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1
        return True
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next    
            
    def make_empty(self):
        self.head = None
        self.length = 0

    # WRITE REVERSE_BETWEEN METHOD HERE #
    #                                   #
    #                                   #
    #                                   #
    #                                   #
    #####################################
    def reverse_between(self, start_index, end_index):
        # if not self.head or not self.head.next:
        #     return None
        
        dummy = Node(0)    
        dummy.next = self.head
        prev = dummy
        
        for _ in range(start_index):
            prev = prev.next
            
        current = prev.next
        # for _ in range(end_index - start_index + 1):
        '''
        具体的实施涉及调整指针：
        temp = current.next 标识要移动的节点。
        current.next = temp.next 在原始位置绕过 temp 节点。
        temp.next = previous.next 让 temp 指向正在被反转的段落的第一个节点（或直接在 previous 之后）。
        previous.next = temp 重新将 temp 连接到列表中，但现在是紧跟在 previous 之后。 
        这一系列指针调整确保了段落的逆转在不丢失链表整体连续性的情况下就地完成。
        '''
        for _ in range(end_index - start_index):
            temp = current.next
            current.next = temp.next
            temp.next = prev.next
            prev.next = temp
        
        self.head = dummy.next


linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

print("Original linked list: ")
linked_list.print_list()

# Reverse a sublist within the linked list
linked_list.reverse_between(2, 4)
print("Reversed sublist (2, 4): ")
linked_list.print_list()

# Reverse another sublist within the linked list
linked_list.reverse_between(0, 4)
print("Reversed entire linked list: ")
linked_list.print_list()

# Reverse a sublist of length 1 within the linked list
linked_list.reverse_between(3, 3)
print("Reversed sublist of length 1 (3, 3): ")
linked_list.print_list()

# Reverse an empty linked list
empty_list = LinkedList(0)
empty_list.make_empty
empty_list.reverse_between(0, 0)
print("Reversed empty linked list: ")
empty_list.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    Original linked list: 
    1
    2
    3
    4
    5
    Reversed sublist (2, 4): 
    1
    2
    5
    4
    3
    Reversed entire linked list: 
    3
    4
    5
    2
    1
    Reversed sublist of length 1 (3, 3): 
    3
    4
    5
    2
    1
    Reversed empty linked list: 
    None
    
"""
