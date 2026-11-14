"""Job sequencing with deadlines."""

def job_sequencing(jobs):
    jobs = sorted(jobs, key=lambda x: x[2], reverse=True)
    max_deadline = max(deadline for _, deadline, _ in jobs)
    slots = [False] * (max_deadline + 1)
    order = []
    profit = 0

    for job_id, deadline, value in jobs:
        for slot in range(min(deadline, max_deadline), 0, -1):
            if not slots[slot]:
                slots[slot] = True
                order.append(job_id)
                profit += value
                break

    return order, profit


def main():
    jobs = [(1, 2, 100), (2, 1, 19), (3, 2, 27), (4, 1, 25), (5, 3, 15)]
    order, profit = job_sequencing(jobs)
    print(f"Selected jobs: {order}")
    print(f"Total profit: {profit}")


if __name__ == "__main__":
    main()
