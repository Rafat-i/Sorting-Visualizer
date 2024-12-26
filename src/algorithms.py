def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            yield arr

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        yield arr  # Yield the current state after partitioning
        yield from quick_sort(arr, low, pi - 1)  # Sort the left part
        yield from quick_sort(arr, pi + 1, high)  # Sort the right part

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def merge_sort(arr):
    # If the array length is less than or equal to 1, it's already sorted
    if len(arr) <= 1:
        yield arr
    else:
        # Split the array in half
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        # Recursively sort both halves
        yield from merge_sort(left)
        yield from merge_sort(right)

        # Merge the two sorted halves
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

        yield arr  # Return the merged sorted array
