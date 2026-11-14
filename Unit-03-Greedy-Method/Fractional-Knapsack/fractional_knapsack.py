def fractional_knapsack(items, capacity):
    items = sorted(items, key=lambda x: x[2] / x[1], reverse=True)
    total_value = 0
    result = []

    for name, weight, value in items:
        if capacity <= 0:
            break
        if weight <= capacity:
            capacity -= weight
            total_value += value
            result.append((name, weight, value))
        else:
            fraction = capacity / weight
            total_value += value * fraction
            result.append((name, weight * fraction, value * fraction))
            break

    return total_value, result


def main():
    items = [
        ("A", 10, 60),
        ("B", 20, 100),
        ("C", 30, 120),
    ]
    capacity = 50
    value, chosen = fractional_knapsack(items, capacity)
    print(f"Maximum value: {value}")
    print(f"Chosen items: {chosen}")


if __name__ == "__main__":
    main()
