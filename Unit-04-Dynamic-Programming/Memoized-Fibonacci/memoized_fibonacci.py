from functools import lru_cache


@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def main():
    n = 10
    print(f"Fibonacci({n}) = {fibonacci(n)}")


if __name__ == "__main__":
    main()
