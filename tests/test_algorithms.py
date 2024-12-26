from src.algorithms import bubble_sort, quick_sort, merge_sort


def test_bubble_sort():
    # Define the array to test
    array = [5, 3, 8, 6, 2]

    # Run the bubble_sort generator
    sorted_array = list(bubble_sort(array))[-1]  # Get the final sorted array

    # Assert that the final sorted array matches Python's built-in sorted()
    assert sorted_array == sorted(array)


def test_quick_sort():
    # Define the array to test
    array = [5, 3, 8, 6, 2]

    # Set low and high bounds for the quick_sort
    low = 0
    high = len(array) - 1

    # Run the quick_sort generator
    sorted_array = list(quick_sort(array, low, high))[-1]  # Get the final sorted array

    # Assert that the final sorted array matches Python's built-in sorted()
    assert sorted_array == sorted(array)


def test_merge_sort():
    # Define the array to test
    array = [5, 3, 8, 6, 2]

    # Run the merge_sort generator
    sorted_array = list(merge_sort(array))[-1]  # Get the final sorted array

    # Assert that the final sorted array matches Python's built-in sorted()
    assert sorted_array == sorted(array)
