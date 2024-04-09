import pytest
from src.rr_scheduler import RRScheduler
from src.process import Process

def test_rr_scheduler():
    # Create some sample processes
    processes = [
        Process("P1", arrival_time=0, burst_time=5, priority=1),
        Process("P2", arrival_time=1, burst_time=3, priority=2),
        Process("P3", arrival_time=2, burst_time=7, priority=3)
    ]

    # Initialize the RR scheduler
    scheduler = RRScheduler()

    # Schedule the processes
    scheduling_output = scheduler.schedule(processes)

    # Verify the scheduling output
    expected_output = """Process ID\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time\n\
P1\t\t0\t\t5\t\t5\t\t10\n\
P2\t\t1\t\t3\t\t4\t\t7\n\
P3\t\t2\t\t7\t\t6\t\t13\n\
\n\
Average Waiting Time: 5.0\n\
Average Turnaround Time: 10.0\n\
"""
    assert scheduling_output.strip() == expected_output.strip()

def test_rr_scheduler_different_quantum():
    # Create some sample processes with different time quantum
    processes = [
        Process("P1", arrival_time=0, burst_time=5, priority=1),
        Process("P2", arrival_time=1, burst_time=3, priority=2),
        Process("P3", arrival_time=2, burst_time=7, priority=3)
    ]

    # Initialize the RR scheduler with a different time quantum
    scheduler = RRScheduler()
    scheduler.time_quantum = 3

    # Schedule the processes
    scheduling_output = scheduler.schedule(processes)

    # Verify the scheduling output
    expected_output = """Process ID\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time\n\
P1\t\t0\t\t5\t\t5\t\t10\n\
P2\t\t1\t\t3\t\t4\t\t7\n\
P3\t\t2\t\t7\t\t6\t\t13\n\
\n\
Average Waiting Time: 5.0\n\
Average Turnaround Time: 10.0\n\
"""
    assert scheduling_output.strip() == expected_output.strip()
