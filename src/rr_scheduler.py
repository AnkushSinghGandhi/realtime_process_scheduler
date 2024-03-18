class RRScheduler:
    def __init__(self):
        self.current_time = 0
        self.time_quantum = 2  # Example time quantum of 2 units

    def schedule(self, tasks):
        print("Round Robin Scheduling:")
        print("Time\tTask")
        while tasks:
            task = tasks.pop(0)
            print(f"{self.current_time}\t{task.name}")
            self.current_time += min(self.time_quantum, task.remaining_time)
            task.remaining_time -= self.time_quantum
            if task.remaining_time > 0:
                tasks.append(task)
        print("Scheduling completed.")