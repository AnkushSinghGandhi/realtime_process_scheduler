from src.fcfs_scheduler import FCFSScheduler
from src.process import Process

def test_fcfs_scheduler_with_empty_input():
    # Initialize the FCFS scheduler
    scheduler = FCFSScheduler()

    # Schedule with an empty list of processes
    scheduling_output = scheduler.schedule([])

    # Verify that the output indicates no processes to schedule
    expected_output = "No processes to schedule"
    assert scheduling_output == expected_output

def test_fcfs_scheduler_with_processes_same_arrival_times():
    # Create some sample processes with the same arrival time
    processes = [
        Process("P1", arrival_time=0, burst_time=5, priority=1),
        Process("P2", arrival_time=0, burst_time=3, priority=2),
        Process("P3", arrival_time=0, burst_time=7, priority=3)
    ]

    # Initialize the FCFS scheduler
    scheduler = FCFSScheduler()

    # Schedule the processes
    scheduling_output = scheduler.schedule(processes)

    # Verify the scheduling output
    expected_output = """Process ID\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time\n\
P1\t\t0\t\t5\t\t0\t\t5\n\
P2\t\t0\t\t3\t\t5\t\t8\n\
P3\t\t0\t\t7\t\t8\t\t15\n\
\n\
Average Waiting Time: 4.333333333333333\n\
Average Turnaround Time: 9.333333333333334\n\
"""
    assert scheduling_output == expected_output

def test_fcfs_scheduler_with_single_process():
    # Create a single sample process
    process = Process("P1", arrival_time=0, burst_time=5, priority=1)

    # Initialize the FCFS scheduler
    scheduler = FCFSScheduler()

    # Schedule the single process
    scheduling_output = scheduler.schedule([process])

    # Verify the scheduling output
    expected_output = """Process ID\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time\n\
P1\t\t0\t\t5\t\t0\t\t5\n\
\n\
Average Waiting Time: 0.0\n\
Average Turnaround Time: 5.0\n\
"""
    assert scheduling_output == expected_output