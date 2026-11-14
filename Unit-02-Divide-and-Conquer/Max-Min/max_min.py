def max_min(arr, start, end):
    if start == end:
        return arr[start], arr[start]

    if end == start + 1:
        if arr[start] < arr[end]:
            return arr[start], arr[end]
        return arr[end], arr[start]

    mid = (start + end) // 2
    left_min, left_max = max_min(arr, start, mid)
    right_min, right_max = max_min(arr, mid + 1, end)

    return min(left_min, right_min), max(left_max, right_max)


def main():
    arr = [7, 2, 9, 4, 1, 6, 8, 3]
    minimum, maximum = max_min(arr, 0, len(arr) - 1)
    print(f"Array: {arr}")
    print(f"Minimum: {minimum}")
    print(f"Maximum: {maximum}")


if __name__ == "__main__":
    main()
