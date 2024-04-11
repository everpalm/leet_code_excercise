'''
Assignment:
Write an insertion_sort() method in the LinkedList class that will sort the elements of a linked list in ascending order using the insertion sort algorithm.

The method should update the head and tail pointers of the linked list to reflect the new order of the nodes in the list.

You can assume that the input linked list will contain only integers. You should not use any additional data structures to sort the linked list.

Input:
The LinkedList object containing a linked list with unsorted elements (self).

Output:
None. The method sorts the linked list in place.

Method Description:
If the length of the linked list is less than 2, the method returns and the list is assumed to be already sorted.
The first element of the linked list is treated as the sorted part of the list, and the second element is treated as the unsorted part of the list.
The first element of the sorted part of the list is then disconnected from the rest of the list, creating a new linked list with only one element.
The method then iterates through each remaining node in the unsorted part of the list.
For each node in the unsorted part of the list, the method determines its correct position in the sorted part of the list by comparing its value with the values of the other nodes in the sorted part of the list.
Once the correct position has been found, the node is inserted into the sorted part of the list at the appropriate position.
After all the nodes in the unsorted part of the list have been inserted into the sorted part of the list, the head and tail pointers of the linked list are updated to reflect the new order of the nodes in the list.

Constraints:
The linked list can contain duplicates.
The method should be implemented in the LinkedList class.
The method should not use any additional data structures to sort the linked list.
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    # WRITE INSERTION_SORT METHOD HERE #
    #                                  #
    #                                  #
    #                                  #
    #                                  #
    ####################################
    # def insertion_sort(self):
        # if self.length < 2:
        #     return
        # prev = self.head
        # while prev is not None:
        #     temp = self.head.next
        #     while temp is not None:
        #         if temp.value < prev.value:
        #             prev.next = temp.next
        #             temp.next = prev
        #             prev = temp
        #             temp = prev.next
        #     return None    
        
        # ChapGPT solution   
        # If the list is empty or has a single element, it's already sorted
        # if self.head is None or self.head.next is None:
        #     return
        
        # sorted_tail = self.head  # The end of the sorted part of the list
        # current = self.head.next  # The current node to insert into the sorted part
        
        # sorted_tail.next = None  # Disconnect the sorted part from the rest
        
        # while current:
        #     next_to_insert = current.next  # Save the next node to be inserted
            
        #     # If the current node is smaller than the head, insert it at the beginning
        #     if current.value <= self.head.value:
        #         current.next = self.head
        #         self.head = current
        #     else:
        #         # Find the correct position for the current node
        #         position = self.head
        #         while position.next is not None and position.next.value < current.value:
        #             position = position.next
                
        #         # Insert the current node into the sorted part
        #         current.next = position.next
        #         position.next = current
                
        #         # If inserting at the end, update the tail
        #         if position == sorted_tail:
        #             sorted_tail = current
            
        #     current = next_to_insert  # Move to the next node to be inserted
        
        # # Update the tail pointer
        # self.tail = sorted_tail
        # if self.tail is not None:
        #     while self.tail.next:
        #         self.tail = self.tail.next

# Commenting out method calls to adhere to instructions
# Let's move to discussing and optimizing this code.              
    def insertion_sort(self):
        # Check if the length of the list is less than 2
        if self.length < 2:
            return
        
        # Set the pointer to the first element of the sorted list
        sorted_list_head = self.head
        print('initial sorted_list_head.value = ', sorted_list_head.value)
        
        # Set the pointer to the second element of the list
        unsorted_list_head = self.head.next
        print('initial unsorted_list_head.value = ', unsorted_list_head.value)
        
        # Remove the first element from the sorted list
        sorted_list_head.next = None
        
        # Iterate through the unsorted list
        while unsorted_list_head is not None:
            # Save the current element
            current = unsorted_list_head
            print('current = ', unsorted_list_head.value)
            
            # Move the pointer to the next element in the unsorted list
            unsorted_list_head = unsorted_list_head.next
            # if unsorted_list_head is not None:
            #     print('unsorted_list_head.value = ', unsorted_list_head.value)
            # else:
            #     print('unsorted ends')
            print('sorted_list_head.value = ', sorted_list_head.value)
            # Insert the current element into the sorted list
            if current.value < sorted_list_head.value:
                # If the current element is smaller than the first element 
                # in the sorted list, it becomes the new first element
                current.next = sorted_list_head
                sorted_list_head = current
                print('After sorted_list_head.value = ', sorted_list_head.value)
            else:
                # Otherwise, search for the appropriate position to insert the current element
                search_pointer = sorted_list_head
                while search_pointer.next is not None and current.value > search_pointer.next.value:
                    search_pointer = search_pointer.next
                current.next = search_pointer.next
                search_pointer.next = current
                if current.next: print('current.next.value = ', current.next.value)
                print('search_pointer.next.value = ', search_pointer.next.value)
        
        # Update the head and tail of the list
        self.head = sorted_list_head
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        self.tail = temp   




my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(1)
my_linked_list.append(3)

print("Linked List Before Sort:")
my_linked_list.print_list()

my_linked_list.insertion_sort()

print("\nSorted Linked List:")
my_linked_list.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    Linked List Before Sort:
    4
    2
    6
    5
    1
    3

    Sorted Linked List:
    1
    2
    3
    4
    5
    6

"""

