import tkinter as tk
from tkinter import font  # Import font module for custom fonts

class Queue:
    def __init__(self):
        self.queue = []
    
    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[0]

    def rear(self):
        if self.is_empty():
            return None
        return self.queue[-1]

    def size(self):
        return len(self.queue)

    def traverse(self):
        return self.queue

class QueueGUI:
    def __init__(self, root):
        self.queue = Queue()
        self.root = root
        # Set the title of the window with the creator's name
        self.root.title("Queue Application Created by Muskan Pandey")
        self.root.geometry("900x600")  # Increased width for more space

        # Define custom fonts
        self.label_font = font.Font(family="Arial", size=15, weight="bold")
        self.button_font = font.Font(family="Arial", size=12)

        # Create two main frames with relative widths
        self.operation_frame = tk.Frame(root, width=500, bg='lightblue')  # Wider frame
        self.operation_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        self.result_frame = tk.Frame(root, width=400, bg='lightgray')  # Narrower frame
        self.result_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Widgets for the operation frame
        self.label = tk.Label(self.operation_frame, text="Queue Application Created by Muskan Pandey", font=self.label_font, bg='lightblue')
        self.label.pack(pady=10)

        self.enqueue_entry = tk.Entry(self.operation_frame, width=30, font=self.button_font)
        self.enqueue_entry.pack(pady=5)

        self.enqueue_button = tk.Button(self.operation_frame, text="Enqueue", command=self.enqueue, font=self.button_font)
        self.enqueue_button.pack(pady=5)

        self.dequeue_button = tk.Button(self.operation_frame, text="Dequeue", command=self.dequeue, font=self.button_font)
        self.dequeue_button.pack(pady=5)

        self.peek_button = tk.Button(self.operation_frame, text="Peek", command=self.peek, font=self.button_font)
        self.peek_button.pack(pady=5)

        self.rear_button = tk.Button(self.operation_frame, text="Rear", command=self.rear, font=self.button_font)
        self.rear_button.pack(pady=5)

        self.size_button = tk.Button(self.operation_frame, text="Queue Size", command=self.show_size, font=self.button_font)
        self.size_button.pack(pady=5)

        self.show_queue_button = tk.Button(self.operation_frame, text="Show Queue", command=self.show_queue, font=self.button_font)
        self.show_queue_button.pack(pady=5)
    
        # Widgets for the result frame
        self.result_listbox = tk.Listbox(self.result_frame, width=50, height=25, font=self.button_font)
        self.result_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(self.result_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.result_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.result_listbox.yview)

    def enqueue(self):
        item = self.enqueue_entry.get()
        if item:
            self.queue.enqueue(item)
            self.enqueue_entry.delete(0, tk.END)
            self.update_result(f"Enqueued: {item}")
        else:
            self.update_result("Please enter a value to enqueue.")

    def dequeue(self):
        item = self.queue.dequeue()
        if item is None:
            self.update_result("Queue is empty. Cannot dequeue.")
        else:
            self.update_result(f"Dequeued: {item}")

    def peek(self):
        item = self.queue.peek()
        if item is None:
            self.update_result("Queue is empty. No front element.")
        else:
            self.update_result(f"Front element: {item}")

    def rear(self):
        item = self.queue.rear()
        if item is None:
            self.update_result("Queue is empty. No rear element.")
        else:
            self.update_result(f"Rear element: {item}")

    def show_queue(self):
        items = self.queue.traverse()
        if not items:
            self.update_result("Queue is empty.")
        else:
            self.update_result(f"Queue contains: {', '.join(items)}")

    def show_size(self):
        size = self.queue.size()
        self.update_result(f"Queue size: {size}")

    def update_result(self, message):
        self.result_listbox.insert(tk.END, message)
        self.result_listbox.yview(tk.END)  # Scroll to the end of the listbox

if __name__ == "__main__":
    root = tk.Tk()
    app = QueueGUI(root)
    root.mainloop()
