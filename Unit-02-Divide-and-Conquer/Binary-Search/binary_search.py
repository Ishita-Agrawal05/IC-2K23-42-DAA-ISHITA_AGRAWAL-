"""Binary Search implementation."""

def binary_search(arr, target):
    """Return the index of target in a sorted array, else -1."""
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def main():
    data = [2, 5, 8, 12, 16, 23, 38, 56, 72]
    target = 23
    index = binary_search(data, target)
    print(f"Sorted array: {data}")
    print(f"Searching for {target}: index {index}")

    print(f"Searching for 99: index {binary_search(data, 99)}")


if __name__ == "__main__":
    main()
