from collections import deque

class RMScheduler:
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
            self.ready_queue = deque(sorted(self.ready_queue, key=lambda x: x.deadline))
            process = self.ready_queue.popleft()
            if process.arrival_time > self.current_time:
                self.current_time = process.arrival_time
            scheduling_output += f"{self.current_time}\t{process.name}\n"
            self.current_time += 1
            if self.current_time > process.deadline:
                scheduling_output += f"{process.name} missed deadline!\n"
            else:
                process.arrival_time += process.arrival_time
                self.ready_queue.append(process)
        
        scheduling_output += "Scheduling completed.\n"
        return scheduling_output
