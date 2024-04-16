'''
Coding Exercise 101
Write a Python function that takes a list of integers as input and returns a
tuple containing the maximum and minimum values in the list.

The function should have the following signature:
def find_max_min(myList):

Where myList is the list of integers to search for the maximum and minimum
values.

The function should traverse the list and keep track of the current maximum
and minimum values. It should then return these values as a tuple, with the
maximum value as the first element and the minimum value as the second
element.

For example, if the input list is [5, 3, 8, 1, 6, 9], the function should
return (9, 1) since 9 is the maximum value and 1 is the minimum value.

'''
# WRITE FIND_MAX_MIN FUNCTION HERE #
#                                  #
#                                  #
#                                  #
#                                  #
####################################
# def find_max_min(myList):
#     # sorted_list = sorted(myList)
#     # min_value = sorted_list[0]
#     # max_value = sorted_list.pop()
#     # return (max_value, min_value)
#     print('Before myList = ', myList)
#     for i in range(len(myList)-1,0,-1):
#         for j in range(i):
#             if myList[j] > myList[j+1]:
#                 myList[j], myList[j+1] = myList[j+1], myList[j]
#     print('After myList = ', myList)
#     max_value = myList[len(myList)-1]
#     min_value = myList[0]
#     return (max_value, min_value)  
def find_max_min(myList):
    # Initialize the maximum and minimum variables 
    # to the first element of the list
    if len(myList) == 0:
        return
    maximum = minimum = myList[0]
    
    # Traverse the list and update the 
    # maximum and minimum variables
    for num in myList:
        if num > maximum:
            maximum = num
        elif num < minimum:
            minimum = num
    # myList = sorted(myList)
    # maximum = myList.pop()
    # minimum = myList.pop(0)
    '''
    Python 的 `sorted()` 函數使用的排序算法是 Timsort，這是一種結合了合併排序（Merge Sort）和插入排序
    （Insertion Sort）的高效排序算法。Timsort 被設計來優化現實世界數據中常見的各種情況，並且對於多數實際
    應用而言，它是非常快速和穩定的。要理解為什麼 `sorted()` 的時間複雜度是 O(n log n)，我們需要考慮合併
    排序的基本運作原理，因為這是 Timsort 的核心部分之一：

    1. **分割**：合併排序首先將數據集分割成越來越小的子集，直至每個子集只包含一個元素。
    2. **合併**：然後將這些子集兩兩合併回去，合併過程中會將它們排序。每次合併操作都需要對元素進行比較和重排，這是一個有序的過程。

    這兩個步驟中，**分割**階段的時間複雜度基本上是 O(log n)，因為每次操作都將數據集分割為兩半，進行了 log n 次分割才達到單個元素的級
    別。而在**合併**階段，每一層的合併操作需要 O(n) 的時間來比較和重新排列元素，而合併操作需要執行 log n 層，因為每次合併都將之前分割
    的部分重新合併起來。因此，合併排序的總時間複雜度是每層 O(n) 與層數 log n 的乘積，即 O(n log n)。

    Timsort 進一步優化了這個過程，它可以在遇到已經部分有序的數據時進行更快的處理。例如，如果數據中已經存在部分有序的區塊，Timsort 會
    利用這些有序的區塊來減少必要的工作量。這使得 Timsort 在最佳情況下的性能可以比 O(n log n) 更好，但平均和最壞情況下，它仍然保持
    O(n log n) 的時間複雜度。
    '''
    # Return the maximum and minimum variables
    return maximum, minimum

print(find_max_min([5, 3, 8, 1, 6, 9]))
print(find_max_min([1, 2, 3, 4, 5, 6]))
print(find_max_min([6, 5, 4, 3, 2, 1]))
print(find_max_min([1, 1, 1, 1, 1, 1]))
print(find_max_min([]))


"""
    EXPECTED OUTPUT:
    ----------------
    (9, 1)
    
"""