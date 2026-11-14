"""Divide-and-conquer maximum and minimum finder."""

def max_min(arr):
    """Return (minimum, maximum) for a non-empty list."""
    if not arr:
        raise ValueError("Array must not be empty")
    if len(arr) == 1:
        return arr[0], arr[0]

    if len(arr) == 2:
        return (arr[0], arr[1]) if arr[0] < arr[1] else (arr[1], arr[0])

    mid = len(arr) // 2
    left_min, left_max = max_min(arr[:mid])
    right_min, right_max = max_min(arr[mid:])

    return min(left_min, right_min), max(left_max, right_max)


def main():
    values = [7, 3, 18, 9, 1, 12, 5, 21]
    minimum, maximum = max_min(values)
    print(f"Array: {values}")
    print(f"Minimum: {minimum}")
    print(f"Maximum: {maximum}")


if __name__ == "__main__":
    main()
