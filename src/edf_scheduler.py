from collections import deque

class EDFScheduler:
    def __init__(self):
        self.current_time = 0
        self.ready_queue = deque()
        self.running_process = None

    def schedule(self, processes):
        if not processes:
            return "No processes to schedule"  # Return a message if there are no processes

        self.ready_queue.extend(processes)

        scheduling_output = "Time\tProcess\n"

        while self.ready_queue:
            self.ready_queue = deque(sorted(self.ready_queue, key=lambda x: x.arrival_time))
            process = self.ready_queue.popleft()
            if process.arrival_time > self.current_time:
                self.current_time = process.arrival_time
            scheduling_output += f"{self.current_time}\t{process.name}\n"
            self.current_time += process.burst_time  # Progress time by burst time
        
        scheduling_output += "Scheduling completed.\n"
        return scheduling_output
