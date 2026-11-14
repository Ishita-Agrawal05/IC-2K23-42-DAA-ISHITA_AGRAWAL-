def backtracking(nums, target, start=0, current=None, result=None):
    if current is None:
        current = []
    if result is None:
        result = []

    total = sum(current)
    if total == target:
        result.append(current.copy())
        return result

    for i in range(start, len(nums)):
        current.append(nums[i])
        backtracking(nums, target, i + 1, current, result)
        current.pop()

    return result


def main():
    nums = [1, 2, 3, 4]
    target = 6
    solutions = backtracking(nums, target)
    print(f"Target: {target}")
    print(f"Solutions: {solutions}")


if __name__ == "__main__":
    main()
