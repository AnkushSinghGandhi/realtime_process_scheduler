from collections import deque

class MFQScheduler:
    def __init__(self, num_queues=3, time_quantum=[4, 8, 16]):
        self.num_queues = num_queues
        self.time_quantum = time_quantum
        self.queues = [deque() for _ in range(num_queues)]
        self.current_time = 0

    def schedule(self, processes):
        if not processes:
            return "No processes to schedule"  # Return a message if there are no processes

        for process in processes:
            self.queues[0].append(process)  # Initially place processes in the highest priority queue

        scheduling_output = "Time\tProcess\n"

        while any(self.queues):
            for i in range(self.num_queues):
                if self.queues[i]:
                    process = self.queues[i].popleft()
                    if process.arrival_time > self.current_time:
                        self.current_time = process.arrival_time
                    scheduling_output += f"{self.current_time}\t{process.name}\n"
                    self.current_time += min(self.time_quantum[i], process.burst_time)
                    process.burst_time -= min(self.time_quantum[i], process.burst_time)
                    if process.burst_time > 0:
                        self.queues[min(i + 1, self.num_queues - 1)].append(process)
                    break

        scheduling_output += "Scheduling completed.\n"
        return scheduling_output
