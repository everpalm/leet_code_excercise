def swap(my_list, index1, index2):
    print("swap!")
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp


# def pivot(my_list, pivot_index, end_index):
#     swap_index = pivot_index
    
#     for i in range(pivot_index+1, end_index+1):
#         print(f"my_list[{i}] = {my_list[i]}")
#         print(f"my_list[{pivot_index}] = {my_list[pivot_index]}")
#         if my_list[i] < my_list[pivot_index]:
#             swap_index += 1
#             print("swap_index = ", swap_index)
#             swap(my_list, swap_index, i)
#     swap(my_list, pivot_index, swap_index)
#     return swap_index
def pivot(my_list, low, high):
    # 將最後一個元素作為 pivot
    pivot_val = my_list[high]
    i = low - 1
    # 遍歷 low 到 high-1 的元素
    for j in range(low, high):
        print(f"my_list[{j}] = {my_list[j]}")
        print(f"pivot_val = {pivot_val}")
        if my_list[j] < pivot_val:
            i += 1
            print("swap_index = ", i)
            swap(my_list, i, j)
    swap(my_list, i + 1, high)
    return i + 1

def quick_sort_helper(my_list, left, right):
    print("my_list = ", my_list)
    if left < right:
        pivot_index = pivot(my_list, left, right)
        quick_sort_helper(my_list, left, pivot_index-1)  
        quick_sort_helper(my_list, pivot_index+1, right)
    return my_list
    

def quick_sort(my_list):
    quick_sort_helper(my_list, 0, len(my_list)-1)

 
 


# my_list = [4,6,1,7,3,2,5]
my_list = [8, 3, 7, 4, 6, 2, 5]

quick_sort(my_list)

print(my_list)



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6, 7]
 """