class PriorityScheduler:
    def __init__(self):
        self.current_time = 0
        self.total_waiting_time = 0
        self.total_turnaround_time = 0

    def schedule(self, processes):
        if not processes:
            return "No processes to schedule"  # Return a message if there are no processes

        # Sort processes based on priority (lower priority number indicates higher priority)
        processes.sort(key=lambda x: x.priority)
        
        scheduling_output = "Process ID\tArrival Time\tPriority\tBurst Time\tWaiting Time\tTurnaround Time\n"
        
        for process in processes:
            # Calculate waiting time
            waiting_time = max(0, self.current_time - process.arrival_time)
            self.total_waiting_time += waiting_time
            # Calculate turnaround time
            turnaround_time = waiting_time + process.burst_time
            self.total_turnaround_time += turnaround_time
            scheduling_output += f"{process.name}\t\t{process.arrival_time}\t\t{process.priority}\t\t{process.burst_time}\t\t{waiting_time}\t\t{turnaround_time}\n"
            # Update current time
            self.current_time += process.burst_time
        
        avg_waiting_time = self.total_waiting_time / len(processes)
        avg_turnaround_time = self.total_turnaround_time / len(processes)
        
        scheduling_output += f"\nAverage Waiting Time: {avg_waiting_time}\n"
        scheduling_output += f"Average Turnaround Time: {avg_turnaround_time}\n"
        
        return scheduling_output  # Return the scheduling output as a string
