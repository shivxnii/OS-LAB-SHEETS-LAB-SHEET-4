# -------- FCFS Scheduling --------
def fcfs(processes):
    print("\n----- FCFS Scheduling -----")
    print("PID\tBT\tWT\tTAT")

    wt = 0
    total_wt = 0
    total_tat = 0

    for pid, bt in processes:
        tat = wt + bt
        print(f"{pid}\t{bt}\t{wt}\t{tat}")
        total_wt += wt
        total_tat += tat
        wt += bt

    print("Average Waiting Time:", total_wt / len(processes))
    print("Average Turnaround Time:", total_tat / len(processes))


# -------- SJF Scheduling (Non-preemptive) --------
def sjf(processes):
    processes.sort(key=lambda x: x[1])  # sort by BT

    print("\n----- SJF Scheduling -----")
    print("PID\tBT\tWT\tTAT")

    wt = 0
    total_wt = 0
    total_tat = 0

    for pid, bt in processes:
        tat = wt + bt
        print(f"{pid}\t{bt}\t{wt}\t{tat}")
        total_wt += wt
        total_tat += tat
        wt += bt

    print("Average Waiting Time:", total_wt / len(processes))
    print("Average Turnaround Time:", total_tat / len(processes))


# -------- Priority Scheduling --------
def priority_scheduling(processes):
    # processes = [(pid, bt, priority)]
    processes.sort(key=lambda x: x[2])  # sort by priority

    print("\n----- Priority Scheduling -----")
    print("PID\tBT\tP\tWT\tTAT")

    wt = 0
    total_wt = 0
    total_tat = 0

    for pid, bt, pr in processes:
        tat = wt + bt
        print(f"{pid}\t{bt}\t{pr}\t{wt}\t{tat}")
        total_wt += wt
        total_tat += tat
        wt += bt

    print("Average Waiting Time:", total_wt / len(processes))
    print("Average Turnaround Time:", total_tat / len(processes))


# -------- Round Robin Scheduling --------
def round_robin(processes, quantum):
    print("\n----- Round Robin Scheduling -----")
    print("PID\tBT\tWT\tTAT")

    n = len(processes)
    rem_bt = [bt for _, bt in processes]
    t = 0
    wt = [0] * n
    tat = [0] * n

    while True:
        complete = True

        for i in range(n):
            if rem_bt[i] > 0:
                complete = False

                if rem_bt[i] > quantum:
                    t += quantum
                    rem_bt[i] -= quantum
                else:
                    t += rem_bt[i]
                    wt[i] = t - processes[i][1]
                    rem_bt[i] = 0

        if complete:
            break

    for i in range(n):
        tat[i] = wt[i] + processes[i][1]
        print(f"{processes[i][0]}\t{processes[i][1]}\t{wt[i]}\t{tat[i]}")

    print("Average Waiting Time:", sum(wt) / n)
    print("Average Turnaround Time:", sum(tat) / n)


# --------- MAIN INPUT ---------

n = int(input("Enter number of processes: "))

processes_fcfs = []
processes_sjf = []
processes_priority = []
processes_rr = []

for i in range(n):
    bt = int(input(f"Enter Burst Time for P{i+1}: "))
    pr = int(input(f"Enter Priority for P{i+1}: "))

    processes_fcfs.append((i + 1, bt))
    processes_sjf.append((i + 1, bt))
    processes_priority.append((i + 1, bt, pr))
    processes_rr.append((i + 1, bt))

quantum = int(input("Enter Time Quantum: "))

fcfs(processes_fcfs)
sjf(processes_sjf)
priority_scheduling(processes_priority)
round_robin(processes_rr, quantum)
