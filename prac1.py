import tkinter as tk
from tkinter import messagebox

class Stack:
    def __init__(self, max_size):
        self.array = []
        self.max_size = max_size
        self.top = -1  # Stack is initially empty

    def push(self, element):
        if self.top < self.max_size - 1:
            self.array.append(element)
            self.top += 1
            return True
        else:
            return False

    def pop(self):
        if self.top >= 0:
            element = self.array.pop()
            self.top -= 1
            return element
        else:
            return None

    def peek(self):
        if self.top >= 0:
            return self.array[self.top]
        else:
            return None

    def display(self):
        return self.array[:self.top + 1]

class StackGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Stack Operations")
        self.master.geometry("400x400")
        self.master.configure(bg="#f0f0f0")

        self.stack = None

        # Title label
        self.title_label = tk.Label(master, text="Stack Operations", font=("Arial", 16), bg="#f0f0f0")
        self.title_label.pack(pady=10)

        # Stack size input
        self.label = tk.Label(master, text="Enter stack size:", bg="#f0f0f0")
        self.label.pack(pady=5)

        self.size_entry = tk.Entry(master)
        self.size_entry.pack(pady=5)

        self.size_button = tk.Button(master, text="Set Size", command=self.set_size, bg="#4CAF50", fg="white")
        self.size_button.pack(pady=10)

        # Push input
        self.push_label = tk.Label(master, text="Value to push:", bg="#f0f0f0")
        self.push_label.pack(pady=5)

        self.push_entry = tk.Entry(master)
        self.push_entry.pack(pady=5)

        self.push_button = tk.Button(master, text="Push", command=self.push, bg="#2196F3", fg="white")
        self.push_button.pack(pady=5)

        # Pop button
        self.pop_button = tk.Button(master, text="Pop", command=self.pop, bg="#F44336", fg="white")
        self.pop_button.pack(pady=5)

        # Peek button
        self.peek_button = tk.Button(master, text="Peek", command=self.peek, bg="#FF9800", fg="white")
        self.peek_button.pack(pady=5)

        # Display stack button
        self.display_button = tk.Button(master, text="Display Stack", command=self.display, bg="#3F51B5", fg="white")
        self.display_button.pack(pady=10)

        # Stack display
        self.stack_display = tk.Label(master, text="Stack: []", font=("Courier New", 12), bg="#f0f0f0")
        self.stack_display.pack(pady=10)

        # Footer
        self.footer_label = tk.Label(master, text="Developed by Muskan Pandey", font=("Arial", 8), bg="#f0f0f0")
        self.footer_label.pack(side=tk.BOTTOM, pady=5)

    def set_size(self):
        try:
            size = int(self.size_entry.get())
            if size <= 0:
                raise ValueError
            self.stack = Stack(size)
            self.update_stack_display()
            messagebox.showinfo("Success", f"Stack size set to {size}")
        except ValueError:
            messagebox.showerror("Error", "Please enter a positive integer for stack size")

    def push(self):
        if self.stack is None:
            messagebox.showerror("Error", "Please set the stack size first.")
            return
        
        item = self.push_entry.get()
        if item:
            if self.stack.push(item):
                self.update_stack_display()
                self.push_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "Stack Overflow: Stack is full")
        else:
            messagebox.showerror("Error", "Please enter a value to push")

    def pop(self):
        if self.stack is None:
            messagebox.showerror("Error", "Please set the stack size first.")
            return
        
        item = self.stack.pop()
        if item is not None:
            self.update_stack_display()
            messagebox.showinfo("Popped", f"Popped item: {item}")
        else:
            messagebox.showerror("Error", "Stack Underflow: Stack is empty")

    def peek(self):
        if self.stack is None:
            messagebox.showerror("Error", "Please set the stack size first.")
            return
        
        item = self.stack.peek()
        if item is not None:
            messagebox.showinfo("Peeked", f"Top item: {item}")
        else:
            messagebox.showinfo("Peek", "Stack is empty")

    def display(self):
        if self.stack is None:
            messagebox.showerror("Error", "Please set the stack size first.")
            return
        
        elements = self.stack.display()
        self.update_stack_display(elements)

    def update_stack_display(self, elements=None):
        if elements is None:
            elements = self.stack.display()
        self.stack_display.config(text=f"Stack: {elements}")

if __name__ == "__main__":
    root = tk.Tk()
    app = StackGUI(root)
    root.mainloop()
