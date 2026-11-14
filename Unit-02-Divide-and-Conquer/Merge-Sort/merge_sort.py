"""Merge sort implementation."""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr[:]

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def main():
    data = [38, 27, 43, 3, 9, 82, 10]
    sorted_data = merge_sort(data)
    print(f"Original: {data}")
    print(f"Sorted:   {sorted_data}")


if __name__ == "__main__":
    main()
