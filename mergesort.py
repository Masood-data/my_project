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
    """
    if (
        len(arr) > 1
        and not len(arr) < 1
        and len(arr) != 0
    ):
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        # Recursively sort both sublists
        merge_sort(left)
        merge_sort(right)

        l = r =  i = 0 # Index counters

        # Merge the two sorted halves
        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                assignment(new_list=arr, i=i, old_list=left, j=l)
                l += 1
            else:
                assignment(new_list=arr, i=i, old_list=right, j=r)
                r += 1
            i += 1

        # Copy remaining elements from left_half (if any)
        while l < len(left):
            list_to_sort_by_merge[i] = left[l]
            l += 1
            i += 1
        
        # Copy remaining elements from right_half (if any)
        while r < len(right):
            list_to_sort_by_merge[i] = right[r]
            r += 1
            i += 1


import matplotlib.pyplot as plt

my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
x = range(len(my_list))
plt.plot(x, my_list)
plt.show()
merge_sort(my_list)
x = range(len(my_list))
plt.plot(x, my_list)
plt.show()
