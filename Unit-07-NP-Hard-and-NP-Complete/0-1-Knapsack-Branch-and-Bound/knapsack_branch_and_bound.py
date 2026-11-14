class Item:
    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value


def bound(item_index, current_weight, current_value, items, capacity):
    if current_weight >= capacity:
        return current_value

    total = current_value
    remaining_capacity = capacity - current_weight
    i = item_index

    while i < len(items) and items[i].weight <= remaining_capacity:
        total += items[i].value
        remaining_capacity -= items[i].weight
        i += 1

    if i < len(items):
        total += items[i].value * (remaining_capacity / items[i].weight)

    return total


def knapsack_branch_and_bound(items, capacity):
    items = sorted(items, key=lambda item: item.value / item.weight, reverse=True)
    best_value = 0
    best_set = []

    def dfs(index, current_weight, current_value, chosen):
        nonlocal best_value, best_set
        if current_weight > capacity:
            return

        if current_value > best_value:
            best_value = current_value
            best_set = chosen.copy()

        if index == len(items):
            return

        if bound(index, current_weight, current_value, items, capacity) <= best_value:
            return

        dfs(index + 1, current_weight + items[index].weight, current_value + items[index].value, chosen + [items[index].name])
        dfs(index + 1, current_weight, current_value, chosen)

    dfs(0, 0, 0, [])
    return best_value, best_set


def main():
    items = [
        Item('A', 10, 60),
        Item('B', 20, 100),
        Item('C', 30, 120),
    ]
    value, chosen = knapsack_branch_and_bound(items, 50)
    print(f"Maximum value: {value}")
    print(f"Chosen items: {chosen}")


if __name__ == "__main__":
    main()
