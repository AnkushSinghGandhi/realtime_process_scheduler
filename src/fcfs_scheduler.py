def fcfs(processes):
    # Sort processes based on arrival time
    processes.sort(key=lambda x: x[1])
    
    current_time = 0
    total_waiting_time = 0
    total_turnaround_time = 0
    
    print("Process ID\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time")
    
    for process in processes:
        pid, arrival_time, burst_time = process
        # Calculate waiting time
        waiting_time = max(0, current_time - arrival_time)
        total_waiting_time += waiting_time
        # Calculate turnaround time
        turnaround_time = waiting_time + burst_time
        total_turnaround_time += turnaround_time
        print(f"{pid}\t\t{arrival_time}\t\t{burst_time}\t\t{waiting_time}\t\t{turnaround_time}")
        # Update current time
        current_time += burst_time
    
    avg_waiting_time = total_waiting_time / len(processes)
    avg_turnaround_time = total_turnaround_time / len(processes)
    
    print(f"\nAverage Waiting Time: {avg_waiting_time}")
    print(f"Average Turnaround Time: {avg_turnaround_time}")

# Example usage:
processes = [
    ("P1", 0, 10),
    ("P2", 6, 20),
    ("P3", 15, 5),
    ("P4", 25, 15)
]
fcfs(processes)
