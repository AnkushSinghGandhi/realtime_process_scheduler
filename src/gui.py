import tkinter as tk
from tkinter import ttk
from src.task import Task
from src.edf_scheduler import EDFScheduler
from src.rms_scheduler import RMScheduler
from collections import deque

class SchedulerGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Scheduler")
        
        self.tasks = []
        self.selected_algorithm = tk.StringVar(value="EDF")
        
        self.create_widgets()
        
    def create_widgets(self):
        self.task_frame = ttk.Frame(self.master)
        self.task_frame.pack(padx=10, pady=10)
        
        self.task_label = ttk.Label(self.task_frame, text="Tasks:")
        self.task_label.grid(row=0, column=0, sticky=tk.W)
        
        self.task_name_label = ttk.Label(self.task_frame, text="Task Name")
        self.task_name_label.grid(row=1, column=0, padx=5)
        self.task_arrival_label = ttk.Label(self.task_frame, text="Arrival Time")
        self.task_arrival_label.grid(row=1, column=1, padx=5)
        self.task_deadline_label = ttk.Label(self.task_frame, text="Deadline")
        self.task_deadline_label.grid(row=1, column=2, padx=5)
        
        self.task_name_entry = ttk.Entry(self.task_frame)
        self.task_name_entry.grid(row=2, column=0, padx=5, pady=5)
        self.task_arrival_entry = ttk.Entry(self.task_frame)
        self.task_arrival_entry.grid(row=2, column=1, padx=5, pady=5)
        self.task_deadline_entry = ttk.Entry(self.task_frame)
        self.task_deadline_entry.grid(row=2, column=2, padx=5, pady=5)
        
        self.add_button = ttk.Button(self.task_frame, text="Add Task", command=self.add_task)
        self.add_button.grid(row=2, column=3, padx=5, pady=5)
        
        self.algorithm_frame = ttk.Frame(self.master)
        self.algorithm_frame.pack(padx=10, pady=10)
        
        self.algorithm_label = ttk.Label(self.algorithm_frame, text="Select Algorithm:")
        self.algorithm_label.grid(row=0, column=0, sticky=tk.W)
        
        self.algorithm_combo = ttk.Combobox(self.algorithm_frame, values=["EDF", "RMS"], textvariable=self.selected_algorithm)
        self.algorithm_combo.grid(row=0, column=1, padx=5, pady=5)
        self.algorithm_combo.bind("<<ComboboxSelected>>", self.on_algorithm_selected)
        
        self.schedule_button = ttk.Button(self.master, text="Schedule", command=self.schedule_tasks)
        self.schedule_button.pack(padx=10, pady=10)
        
        self.output_frame = ttk.Frame(self.master)
        self.output_frame.pack(padx=10, pady=10)
        
        self.output_label = ttk.Label(self.output_frame, text="Output:")
        self.output_label.grid(row=0, column=0, sticky=tk.W)
        
        self.output_text = tk.Text(self.output_frame, width=50, height=10)
        self.output_text.grid(row=1, column=0, padx=5, pady=5)
        self.output_text.configure(state="disabled")
        
    def add_task(self):
        name = self.task_name_entry.get()
        arrival_time = int(self.task_arrival_entry.get())
        deadline = int(self.task_deadline_entry.get())
        task = Task(name, arrival_time, deadline)
        self.tasks.append(task)
        self.task_name_entry.delete(0, tk.END)
        self.task_arrival_entry.delete(0, tk.END)
        self.task_deadline_entry.delete(0, tk.END)
        self.task_name_entry.focus_set()
        
    def on_algorithm_selected(self, event):
        algorithm = self.selected_algorithm.get()
        print(f"Algorithm selected: {algorithm}")
        
    def schedule_tasks(self):
        algorithm = self.selected_algorithm.get()
        self.output_text.configure(state="normal")
        self.output_text.delete(1.0, tk.END)
        if algorithm == "EDF":
            scheduler = EDFScheduler()
        elif algorithm == "RMS":
            scheduler = RMScheduler()
        scheduler.schedule(self.tasks)
        self.output_text.configure(state="disabled")
