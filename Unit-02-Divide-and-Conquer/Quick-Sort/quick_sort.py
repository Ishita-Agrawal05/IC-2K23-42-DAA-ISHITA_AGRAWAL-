"""Quick sort implementation."""

def quick_sort(arr):
    if len(arr) <= 1:
        return arr[:]

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def main():
    data = [9, 4, 7, 2, 8, 1, 6, 5]
    print(f"Original: {data}")
    print(f"Sorted:   {quick_sort(data)}")


if __name__ == "__main__":
    main()
