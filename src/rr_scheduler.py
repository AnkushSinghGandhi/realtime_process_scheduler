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
        
        scheduling_output = "Process ID\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time\n"
        
        while True:
            done = True
            for process in processes:
                if remaining_burst_time[processes.index(process)] > 0:
                    done = False
                    if remaining_burst_time[processes.index(process)] > self.time_quantum:
                        self.current_time += self.time_quantum
                        remaining_burst_time[processes.index(process)] -= self.time_quantum
                    else:
                        self.current_time += remaining_burst_time[processes.index(process)]
                        process_waiting_time = max(0, self.current_time - process.arrival_time - process.burst_time)
                        self.total_waiting_time += process_waiting_time
                        remaining_burst_time[processes.index(process)] = 0
                        process_turnaround_time = self.current_time - process.arrival_time
                        self.total_turnaround_time += process_turnaround_time
                        scheduling_output += f"{process.name}\t\t{process.arrival_time}\t\t{process.burst_time}\t\t{process_waiting_time}\t\t{process_turnaround_time}\n"
            if done:
                break
        
        avg_waiting_time = self.total_waiting_time / len(processes)
        avg_turnaround_time = self.total_turnaround_time / len(processes)
        
        scheduling_output += f"\nAverage Waiting Time: {avg_waiting_time}\n"
        scheduling_output += f"Average Turnaround Time: {avg_turnaround_time}\n"

        return scheduling_output
