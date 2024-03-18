class PriorityScheduler:
    def __init__(self):
        self.current_time = 0

    def schedule(self, tasks):
        print("Priority Scheduling:")
        print("Time\tTask")
        tasks.sort(key=lambda x: x.priority)
        for task in tasks:
            print(f"{self.current_time}\t{task.name}")
            self.current_time += 1
        print("Scheduling completed.")
