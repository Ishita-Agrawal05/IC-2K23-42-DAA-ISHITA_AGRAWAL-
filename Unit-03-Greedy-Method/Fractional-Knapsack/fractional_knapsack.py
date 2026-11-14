"""Fractional knapsack using value-to-weight ratio."""

def fractional_knapsack(items, capacity):
    items = sorted(items, key=lambda x: x[2] / x[1], reverse=True)
    total_value = 0.0
    total_weight = 0
    selected = []

    for name, weight, value in items:
        if total_weight + weight <= capacity:
            total_weight += weight
            total_value += value
            selected.append((name, weight, value, 1.0))
        else:
            remaining = capacity - total_weight
            fraction = remaining / weight
            total_value += value * fraction
            selected.append((name, weight, value, fraction))
            break

    return total_value, selected


def main():
    items = [
        ("A", 10, 60),
        ("B", 20, 100),
        ("C", 30, 120),
    ]
    capacity = 50
    value, chosen = fractional_knapsack(items, capacity)
    print(f"Capacity: {capacity}")
    print(f"Maximum value: {value:.2f}")
    print("Chosen items:", chosen)


if __name__ == "__main__":
    main()
