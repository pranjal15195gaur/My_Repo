def binary_search_iterative(arr, target):
    """Performs iterative binary search on a sorted array."""
    left, right = 0, len(arr) - 1  # Define search boundaries

    while left <= right:
        mid = (left + right) // 2  # Find middle index

        if arr[mid] == target:
            return mid  # Target found, return index
        elif arr[mid] < target:
            left = mid + 1  # Search right half
        else:
            right = mid - 1  # Search left half

    return -1  # Target not found

def binary_search_recursive(arr, left, right, target):
    """Performs recursive binary search on a sorted array."""
    if left > right:
        return -1  # Base case: target not found

    mid = (left + right) // 2  # Find middle index

    if arr[mid] == target:
        return mid  # Target found, return index
    elif arr[mid] < target:
        return binary_search_recursive(arr, mid + 1, right, target)  # Search right half
    else:
        return binary_search_recursive(arr, left, mid - 1, target)  # Search left half

def main():
    """Main function to run binary search on a sample array."""
    arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]  # Sorted array
    target = int(input("Enter target number: "))  # User input for target

    print("\nIterative Binary Search:")
    result_iter = binary_search_iterative(arr, target)  # Run iterative search
    print(f"Element found at index {result_iter}" if result_iter != -1 else "Element not found")

    print("\nRecursive Binary Search:")
    result_rec = binary_search_recursive(arr, 0, len(arr) - 1, target)  # Run recursive search
    print(f"Element found at index {result_rec}" if result_rec != -1 else "Element not found")

if __name__ == "__main__":
    main()  # Run the script

