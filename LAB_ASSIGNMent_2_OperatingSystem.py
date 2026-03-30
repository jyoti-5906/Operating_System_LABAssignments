# ---------------------------------------------
# Banker's Algorithm - Complete Implementation
# Covers Task 1 to Task 5
# ---------------------------------------------

def input_data():
    # Task 1: System Input
    n = int(input("Enter number of processes: "))
    m = int(input("Enter number of resources: "))

    allocation = []
    print("\nEnter Allocation Matrix:")
    for i in range(n):
        allocation.append(list(map(int, input(f"P{i}: ").split())))

    maximum = []
    print("\nEnter Maximum Matrix:")
    for i in range(n):
        maximum.append(list(map(int, input(f"P{i}: ").split())))

    print("\nEnter Available Resources:")
    available = list(map(int, input().split()))

    return n, m, allocation, maximum, available


def calculate_need(n, m, allocation, maximum):
    # Task 2: Need Matrix Calculation
    need = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(maximum[i][j] - allocation[i][j])
        need.append(row)

    print("\nNeed Matrix:")
    for i in range(n):
        print(f"P{i}: {need[i]}")

    return need


def safety_algorithm(n, m, allocation, need, available):
    # Task 3 & 4: Safety Algorithm + Safe Sequence
    work = available.copy()
    finish = [False] * n
    safe_sequence = []

    while len(safe_sequence) < n:
        found = False

        for i in range(n):
            if not finish[i]:
                if all(need[i][j] <= work[j] for j in range(m)):
                    print(f"\nP{i} is executing...")

                    for j in range(m):
                        work[j] += allocation[i][j]

                    safe_sequence.append(f"P{i}")
                    finish[i] = True
                    found = True

                    print(f"Updated Available (Work): {work}")

        if not found:
            break

    return finish, safe_sequence


def result_analysis(n, finish, safe_sequence):
    # Task 5: Result Analysis
    print("\n--- Result ---")

    if all(finish):
        print("System is in SAFE state ")
        print("Safe Sequence:", " -> ".join(safe_sequence))
        print("\nExplanation: All processes completed successfully without deadlock.")
    else:
        print("System is in UNSAFE state ")
        print("\nExplanation: Deadlock may occur as not all processes could complete.")


# ---------------- MAIN PROGRAM ----------------
def main():
    n, m, allocation, maximum, available = input_data()
    need = calculate_need(n, m, allocation, maximum)
    finish, safe_sequence = safety_algorithm(n, m, allocation, need, available)
    result_analysis(n, finish, safe_sequence)


# Run Program
main()