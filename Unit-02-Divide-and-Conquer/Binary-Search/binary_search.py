def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

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
    arr = [2, 4, 7, 9, 12, 15, 18, 21]
    target = 15
    index = binary_search(arr, target)
    print(f"Array: {arr}")
    print(f"Target: {target}")
    print(f"Index: {index}")


if __name__ == "__main__":
    main()
