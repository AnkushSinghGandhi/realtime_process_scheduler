import tkinter as tk
from src.gui import SchedulerGUI

def main():
    root = tk.Tk()
    app = SchedulerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
