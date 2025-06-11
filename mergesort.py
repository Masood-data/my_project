from typing import List
def assignment(new_list: List, index_new: int, old_list: List, index_old: int) -> None:
    """
    Assigns a value from old_list to new_list at specified positions.
    
    Args:
        new_list (List): The list to update.
        index_new (int): Index in new_list.
        old_list (List): The source list.
        index_old (int): Index in old_list.
    """
    new_list[index_new] = old_list[index_old]


def merge_sort(arr: List) -> None:
    """
    Sorts a list in-place using the merge sort algorithm.

    Args:
        arr (List): The list to be sorted.
    Returns:
        None: The list is sorted in-place.
    """
    if (
        len(arr) > 1
        and not len(arr) < 1
        and len(arr) != 0
    ):
        # Divide the list into two halves.
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        # Recursively sort both sublists
        merge_sort(left_half)
        merge_sort(right_half)

        left_index = right_index =  merged_list_index = 0 # Index counters

        # Merge the two sorted halves
        while left_index < len(left_half) and right_index < len(right_half):
            if left_half[left_index] <= right_half[right_index]:
                assignment(new_list=arr, index_new=merged_list_index, old_list=left_half, index_old=left_index)
                left_index += 1
            else:
                assignment(new_list=arr, index_new=merged_list_index, old_list=right_half, index_old=right_index)
                right_index += 1
            merged_list_index += 1

        # Copy remaining elements from left_half (if any)
        while left_index < len(left_half):
            arr[merged_list_index] = left_half[left_index]
            left_index += 1
            merged_list_index += 1
        
        # Copy remaining elements from right_half (if any)
        while right_index < len(right_half):
            arr[merged_list_index] = right_half[right_index]
            right_index += 1
            merged_list_index += 1


import matplotlib.pyplot as plt

my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
x = range(len(my_list))
plt.plot(x, my_list)
plt.show()
merge_sort(my_list)
x = range(len(my_list))
plt.plot(x, my_list)
plt.show()
