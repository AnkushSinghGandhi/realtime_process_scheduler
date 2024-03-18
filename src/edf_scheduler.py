from collections import deque

class EDFScheduler:
    def __init__(self):
        self.current_time = 0
        self.ready_queue = deque()
        self.running_task = None

    def schedule(self, tasks):
        self.ready_queue.extend(tasks)

        print("Time\tTask")
        while self.ready_queue:
            self.ready_queue = deque(sorted(self.ready_queue, key=lambda x: x.deadline))
            task = self.ready_queue.popleft()
            if task.arrival_time > self.current_time:
                self.current_time = task.arrival_time
            print(f"{self.current_time}\t{task.name}")
            self.current_time += 1
            if self.current_time > task.deadline:
                print(f"{task.name} missed deadline!")
            else:
                task.arrival_time += task.arrival_time
                self.ready_queue.append(task)
        print("Scheduling completed.")
