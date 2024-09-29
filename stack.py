import tkinter as tk
from tkinter import messagebox

class Stack:
    """
    A class to represent a stack

    Attributes:
        items: A list to store the stack elements
    """

    def __init__(self):
        """
        Initializes the stack with an empty list
        """
        self.items = []

    def is_empty(self):
        """
        Returns True if the stack is empty, False otherwise
        """
        return len(self.items) == 0

    def push(self, data):
        """
        Inserts an element onto the top of the stack
        """
        self.items.append(data)

    def pop(self):
        """
        Removes and returns the element from the top of the stack
        """
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        """
        Returns the element at the top of the stack without removing it
        """
        if self.is_empty():
            return None
        return self.items[-1]

    def size(self):
        """
        Returns the number of elements in the stack
        """
        return len(self.items)

    def print_stack(self):
        """
        Returns a string representation of the stack elements from top to bottom
        """
        return "\n".join(reversed(self.items))

class StackGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Stack Operations")
        self.master.geometry("600x650")
        self.master.configure(bg="#f0f0f0")

        self.stack = Stack()

        # Title label
        self.title_label = tk.Label(master, text="Stack Operations", font=("Arial", 16), bg="#f0f0f0")
        self.title_label.pack(pady=10)

        # Push input
        self.push_label = tk.Label(master, text="Value to push:", bg="#f0f0f0")
        self.push_label.pack(pady=5)

        self.push_entry = tk.Entry(master)
        self.push_entry.pack(pady=5)

        self.push_button = tk.Button(master, text="Push", command=self.push, bg="#4CAF50", fg="white")
        self.push_button.pack(pady=5)

        # Pop button
        self.pop_button = tk.Button(master, text="Pop", command=self.pop, bg="#F44336", fg="white")
        self.pop_button.pack(pady=5)

        # Peek button
        self.peek_button = tk.Button(master, text="Peek", command=self.peek, bg="#FF9800", fg="white")
        self.peek_button.pack(pady=5)

        # Size button
        self.size_button = tk.Button(master, text="Size", command=self.size, bg="#2196F3", fg="white")
        self.size_button.pack(pady=5)

        # Display stack button
        self.display_button = tk.Button(master, text="Display Stack", command=self.display, bg="#3F51B5", fg="white")
        self.display_button.pack(pady=10)

        # Stack display
        self.stack_display = tk.Label(master, text="Stack: []", font=("Courier New", 12), bg="#f0f0f0")
        self.stack_display.pack(pady=10)

        # Developer info
        self.footer_label = tk.Label(master, text="Application created by Muskan Pandey", font=("Arial", 10), bg="#f0f0f0")
        self.footer_label.pack(side=tk.BOTTOM, pady=5)

    def push(self):
        item = self.push_entry.get()
        if item:
            self.stack.push(item)
            self.update_stack_display()
            self.push_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter a value to push")

    def pop(self):
        item = self.stack.pop()
        if item is not None:
            messagebox.showinfo("Popped", f"Popped item: {item}")
            self.update_stack_display()
        else:
            messagebox.showerror("Error", "Stack Underflow: Stack is empty")

    def peek(self):
        item = self.stack.peek()
        if item is not None:
            messagebox.showinfo("Peeked", f"Top item: {item}")
        else:
            messagebox.showinfo("Peek", "Stack is empty")

    def size(self):
        size = self.stack.size()
        messagebox.showinfo("Stack Size", f"Current stack size: {size}")

    def display(self):
        elements = self.stack.print_stack()
        messagebox.showinfo("Stack Elements", f"Stack elements:\n{elements}" if elements else "Stack is empty")

    def update_stack_display(self):
        self.stack_display.config(text=f"Stack: {self.stack.items}")

if __name__ == "__main__":
    root = tk.Tk()
    app = StackGUI(root)
    root.mainloop()
