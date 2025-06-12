from typing import List
import matplotlib.pyplot as plt


def assign_value(new_list: List, index_new: int, old_list: List, index_old: int) -> None:
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
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively sort both sublists
        merge_sort(left_half)
        merge_sort(right_half)

        i = l = r = 0  # Index counters

        # Merge the two sorted halves
        while l < len(left_half) and r < len(right_half):
            if left_half[l] <= right_half[r]:
                assign_value(arr, i, left_half, l)
                l += 1
            else:
                assign_value(arr, i, right_half, r)
                r += 1
            i += 1

        # Copy remaining elements from left_half (if any)
        while l < len(left_half):
            arr[i] = left_half[l]
            l += 1
            i += 1

        # Copy remaining elements from right_half (if any)
        while r < len(right_half):
            arr[i] = right_half[r]
            r += 1
            i += 1
            
def visualize_list(data, title="List Visualization"):
    """
    Plots the given list using matplotlib.

    Args:
        data (list): The list to be plotted.
        title (str): The title of the plot.
    """
    
    x_coords = range(len(data))
    plt.figure(figsize=(10, 6)) # Set figure size for better readability.
    plt.plot(x_coords, data, marker='o', linestyle='-', color='skyblue') # Add marker and color for clarity.
    plt.title(title)
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.grid(True)
    plt.show()
if __name__ == "__main__":
    # Example usage
    my_list_to_sort = [54, 26, 93, 17, 77, 31, 44, 55, 20]

    print("Original list:", my_list_to_sort)
    visualize_list(my_list_to_sort, "Original List")

    merge_sort(my_list_to_sort)

    print("Sorted list:", my_list_to_sort)
    visualize_list(my_list_to_sort, "Sorted List (Merge Sort)")
