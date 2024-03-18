class SJFScheduler:
    def __init__(self):
        self.current_time = 0

    def schedule(self, tasks):
        print("SJF Scheduling:")
        print("Time\tTask")
        tasks.sort(key=lambda x: x.remaining_time)
        for task in tasks:
            print(f"{self.current_time}\t{task.name}")
            self.current_time += task.remaining_time
        print("Scheduling completed.")