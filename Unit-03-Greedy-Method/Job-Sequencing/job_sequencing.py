# Pseudocode:
# JobSequencing(jobs, deadline_limit)
#     sort jobs by profit in descending order
#     create slots[1..deadline_limit] as empty
#     total_profit = 0
#     sequence = []
#
#     for each job in sorted jobs:
#         for time from min(deadline, deadline_limit) down to 1:
#             if slots[time] is empty:
#                 place job at time
#                 total_profit = total_profit + profit
#                 append job to sequence
#                 break
#
#     return sequence, total_profit


def job_sequencing(jobs, deadline_limit):
    jobs = sorted(jobs, key=lambda x: x[2], reverse=True)
    slots = [None] * (deadline_limit + 1)
    total_profit = 0
    sequence = []

    for job, deadline, profit in jobs:
        for i in range(min(deadline, deadline_limit), 0, -1):
            if slots[i] is None:
                slots[i] = job
                total_profit += profit
                sequence.append(job)
                break

    return sequence, total_profit


def main():
    jobs = [
        ("J1", 2, 100),
        ("J2", 1, 50),
        ("J3", 2, 200),
        ("J4", 3, 150),
    ]
    sequence, profit = job_sequencing(jobs, 3)
    print(f"Sequence: {sequence}")
    print(f"Total profit: {profit}")


if __name__ == "__main__":
    main()
