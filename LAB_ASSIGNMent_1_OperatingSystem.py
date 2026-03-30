# -------- Task 1: Process Class --------
class Process:
    def __init__(self, pid, at, bt):
        self.pid = pid
        self.at = at
        self.bt = bt
        self.ct = 0
        self.tat = 0
        self.wt = 0


# -------- Input Function --------
def take_input():
    n = int(input("Enter number of processes: "))
    processes = []

    for i in range(n):
        at = int(input(f"Arrival Time of P{i+1}: "))
        bt = int(input(f"Burst Time of P{i+1}: "))
        processes.append(Process(i+1, at, bt))

    print("\nPID\tAT\tBT")
    for p in processes:
        print(f"P{p.pid}\t{p.at}\t{p.bt}")

    return processes


# -------- Task 2: FCFS --------
def fcfs(processes):
    pro = sorted(processes, key=lambda x: x.at)
    time = 0

    print("\n--- FCFS ---")
    print("PID\tAT\tBT\tCT\tTAT\tWT")

    total_wt = total_tat = 0

    for p in pro:
        if time < p.at:
            time = p.at

        time += p.bt
        p.ct = time
        p.tat = p.ct - p.at
        p.wt = p.tat - p.bt

        total_wt += p.wt
        total_tat += p.tat

        print(f"P{p.pid}\t{p.at}\t{p.bt}\t{p.ct}\t{p.tat}\t{p.wt}")

    print("Average WT =", total_wt/len(pro))
    print("Average TAT =", total_tat/len(pro))

    return pro


# -------- Task 3: SJF --------
def sjf(processes):
    pro = processes[:]
    completed = []
    time = 0

    print("\n--- SJF ---")
    print("PID\tAT\tBT\tCT\tTAT\tWT")

    total_wt = total_tat = 0

    while pro:
        ready = [p for p in pro if p.at <= time]

        if not ready:
            time += 1
            continue

        ready.sort(key=lambda x: x.bt)
        p = ready[0]

        time += p.bt
        p.ct = time
        p.tat = p.ct - p.at
        p.wt = p.tat - p.bt

        total_wt += p.wt
        total_tat += p.tat

        print(f"P{p.pid}\t{p.at}\t{p.bt}\t{p.ct}\t{p.tat}\t{p.wt}")

        completed.append(p)
        pro.remove(p)

    print("Average WT =", total_wt/len(completed))
    print("Average TAT =", total_tat/len(completed))

    return completed


# -------- Task 4: Gantt Chart --------
def gantt(process_list, name):
    print(f"\nGantt Chart ({name}):")
    for p in process_list:
        print(f"| P{p.pid} ", end="")
    print("|")


# -------- Task 5: Main --------
if __name__ == "__main__":
    processes = take_input()

    fcfs_result = fcfs(processes)
    gantt(fcfs_result, "FCFS")

    sjf_result = sjf(processes)
    gantt(sjf_result, "SJF")

    print("\n--- Comparison ---")
    fcfs_wt = sum(p.wt for p in fcfs_result) / len(fcfs_result)
    sjf_wt = sum(p.wt for p in sjf_result) / len(sjf_result)

    if sjf_wt < fcfs_wt:
        print("SJF is better (less waiting time)")
    else:
        print("FCFS is better")