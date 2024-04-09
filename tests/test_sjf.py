from src.sjf_scheduler import SJFScheduler
from src.process import Process

def test_sjf_scheduler():
    # Create some sample processes
    processes = [
        Process("P1", arrival_time=0, burst_time=5, priority=1),
        Process("P2", arrival_time=1, burst_time=3, priority=2),
        Process("P3", arrival_time=2, burst_time=7, priority=3)
    ]

    # Initialize the SJF scheduler
    scheduler = SJFScheduler()

    # Schedule the processes
    scheduling_output = scheduler.schedule(processes)

    # Verify the scheduling output
    expected_output = """Process ID\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time\n\
P1\t\t0\t\t5\t\t0\t\t5\n\
P2\t\t1\t\t3\t\t4\t\t7\n\
P3\t\t2\t\t7\t\t10\t\t17\n\
\n\
Average Waiting Time: 4.666666666666667\n\
Average Turnaround Time: 9.666666666666666\n\
"""
    assert scheduling_output == expected_output
