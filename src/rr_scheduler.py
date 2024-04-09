class RRScheduler:
    def __init__(self):
        self.current_time = 0
        self.time_quantum = 2  # Example time quantum of 2 units
        self.total_waiting_time = 0
        self.total_turnaround_time = 0

    def schedule(self, processes):
        if not processes:
            return "No processes to schedule"  # Return a message if there are no processes
        
        remaining_burst_time = [process.burst_time for process in processes]  # Using process object attributes
        waiting_times = [0] * len(processes)
        
        scheduling_output = "Process ID\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time\n"
        
        while True:
            done = True
            for i, process in enumerate(processes):
                if remaining_burst_time[i] > 0:
                    done = False
                    if remaining_burst_time[i] > self.time_quantum:
                        self.current_time += self.time_quantum
                        remaining_burst_time[i] -= self.time_quantum
                        waiting_times[i] += self.current_time - process.arrival_time  # Update waiting time
                    else:
                        self.current_time += remaining_burst_time[i]
                        waiting_times[i] += self.current_time - process.arrival_time - remaining_burst_time[i]  # Update waiting time
                        remaining_burst_time[i] = 0
                        process_turnaround_time = self.current_time - process.arrival_time
                        self.total_turnaround_time += process_turnaround_time
                        scheduling_output += f"{process.name}\t\t{process.arrival_time}\t\t{process.burst_time}\t\t{waiting_times[i]}\t\t{process_turnaround_time}\n"
            if done:
                break
        
        self.total_waiting_time = sum(waiting_times)
        avg_waiting_time = self.total_waiting_time / len(processes)
        avg_turnaround_time = self.total_turnaround_time / len(processes)
        
        scheduling_output += f"\nAverage Waiting Time: {avg_waiting_time}\n"
        scheduling_output += f"Average Turnaround Time: {avg_turnaround_time}\n"

        return scheduling_output
