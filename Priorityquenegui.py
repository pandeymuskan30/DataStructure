import tkinter as tk
from tkinter import font

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data, priority):
        index = 0
        while index < len(self.queue) and self.queue[index][1] < priority:
            index += 1
        self.queue.insert(index, (data, priority))

    def is_empty(self):
        return len(self.queue) == 0

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)[0]

    def size(self):
        return len(self.queue)

    def traverse(self):
        return self.queue

class PriorityQueueGUI:
    def __init__(self, root):
        self.queue = PriorityQueue()
        self.root = root
        self.root.title("Priority Queue Application")
        self.root.geometry("900x600")

        self.label_font = font.Font(family="Arial", size=15, weight="bold")
        self.button_font = font.Font(family="Arial", size=12)

        self.operation_frame = tk.Frame(root, width=500, bg='lightblue')
        self.operation_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        self.result_frame = tk.Frame(root, width=400, bg='lightgray')
        self.result_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.label = tk.Label(self.operation_frame, text="Priority Queue Application Created by Muskan.", font=self.label_font, bg='lightblue')
        self.label.pack(pady=10)

        self.item_entry = tk.Entry(self.operation_frame, width=30, font=self.button_font)
        self.item_entry.pack(pady=5)

        self.label = tk.Label(self.operation_frame, text="Priority", font=self.label_font, bg='lightblue')
        self.label.pack(pady=5)

        self.priority_entry = tk.Entry(self.operation_frame, width=10, font=self.button_font)
        self.priority_entry.pack(pady=5)

        self.enqueue_button = tk.Button(self.operation_frame, text="Enqueue", command=self.enqueue, font=self.button_font)
        self.enqueue_button.pack(pady=5)

        self.dequeue_button = tk.Button(self.operation_frame, text="Dequeue", command=self.dequeue, font=self.button_font)
        self.dequeue_button.pack(pady=5)

        self.size_button = tk.Button(self.operation_frame, text="Queue Size", command=self.show_size, font=self.button_font)
        self.size_button.pack(pady=5)

        self.show_queue_button = tk.Button(self.operation_frame, text="Show Queue", command=self.show_queue, font=self.button_font)
        self.show_queue_button.pack(pady=5)

        self.is_empty_button = tk.Button(self.operation_frame, text="Is Empty", command=self.is_empty, font=self.button_font)
        self.is_empty_button.pack(pady=5)

        self.result_listbox = tk.Listbox(self.result_frame, width=50, height=25, font=self.button_font)
        self.result_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(self.result_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.result_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.result_listbox.yview)

    def enqueue(self):
        item = self.item_entry.get()
        priority = self.priority_entry.get()
        if item and priority:
            try:
                priority = int(priority)
                self.queue.enqueue(item, priority)
                self.update_result(f"Enqueued: {item} with Priority: {priority}")
                self.item_entry.delete(0, tk.END)
                self.priority_entry.delete(0, tk.END)
            except ValueError:
                self.update_result("Priority must be an integer.")
        else:
            self.update_result("Please enter a value and priority to enqueue.")

    def dequeue(self):
        item = self.queue.dequeue()
        if item is None:
            self.update_result("Queue is empty. Cannot dequeue.")
        else:
            self.update_result(f"Dequeued: {item}")

    def show_size(self):
        size = self.queue.size()
        self.update_result(f"Queue size: {size}")

    def show_queue(self):
        items = self.queue.traverse()
        if not items:
            self.update_result("Queue is empty.")
        else:
            self.update_result("Queue contains:")
            for item, priority in items:
                self.update_result(f"Item: {item}, Priority: {priority}")

    def is_empty(self):
        empty = self.queue.is_empty()
        self.update_result(f"Priority Queue is empty: {empty}")

    def update_result(self, message):
        self.result_listbox.insert(tk.END, message)
        self.result_listbox.yview(tk.END)  # Scroll to the end of the listbox

if __name__ == "__main__":
    root = tk.Tk()
    app = PriorityQueueGUI(root)
    root.mainloop()
