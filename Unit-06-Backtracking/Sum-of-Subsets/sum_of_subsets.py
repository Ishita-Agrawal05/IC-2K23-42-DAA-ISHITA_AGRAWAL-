def sum_of_subsets(nums, target):
    result = []

    def backtrack(start, chosen, remaining):
        if remaining == 0:
            result.append(chosen.copy())
            return
        if start == len(nums) or remaining < 0:
            return

        for i in range(start, len(nums)):
            chosen.append(nums[i])
            backtrack(i + 1, chosen, remaining - nums[i])
            chosen.pop()

    backtrack(0, [], target)
    return result


def main():
    nums = [3, 5, 6, 10]
    target = 11
    print(sum_of_subsets(nums, target))


if __name__ == "__main__":
    main()
