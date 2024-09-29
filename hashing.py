import tkinter as tk
from tkinter import messagebox

class Node:
    def __init__(self, key, value):
        """Node for the linked list used in overflow chaining."""
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size):
        """Initialize the hash table with a given size."""
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        """Hash function to determine the index for a given key."""
        return key % self.size

    def insert(self, key, value):
        """Insert a key-value pair into the hash table."""
        index = self.hash_function(key)
        new_node = Node(key, value)

        if self.table[index] is None:
            self.table[index] = new_node
        else:
            current = self.table[index]
            while current.next:
                current = current.next
            current.next = new_node

    def delete(self, key):
        """Delete the value associated with the given key."""
        index = self.hash_function(key)
        current = self.table[index]
        prev = None

        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.table[index] = current.next
                return
            prev = current
            current = current.next

    def search(self, key):
        """Search for the value associated with the given key."""
        index = self.hash_function(key)
        current = self.table[index]

        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def traverse(self):
        """Traverse and print all key-value pairs in the hash table."""
        all_elements = []
        for index, node in enumerate(self.table):
            current = node
            while current:
                all_elements.append(f"Index {index}: Key {current.key}, Value {current.value}")
                current = current.next
        return all_elements

class HashTableApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hash Table")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f8ff")  # Light Alice Blue
        self.hash_table = None

        # Header Frame
        header_frame = tk.Frame(self.root, bg="#add8e6")  # Light Blue
        header_frame.pack(fill=tk.X, padx=10, pady=10)

        # Title Label
        header_label = tk.Label(header_frame, text="Hash Table Application", font=("Arial", 20, "bold"), bg="#add8e6")
        header_label.pack(pady=5)

        # Creator Label
        creator_label = tk.Label(header_frame, text="Application created by Muskan Pandey", font=("Arial", 14), bg="#add8e6")
        creator_label.pack(pady=5)

        input_frame = tk.Frame(self.root, bg="#f0f8ff")
        input_frame.pack(pady=10)

        size_label = tk.Label(input_frame, text="Table Size:", font=("Arial", 14), bg="#f0f8ff", fg="#000080")  # Dark Blue
        size_label.grid(row=0, column=0, padx=5, pady=5)
        self.size_entry = tk.Entry(input_frame, font=("Arial", 14))
        self.size_entry.grid(row=0, column=1, padx=5, pady=5)
        set_size_button = tk.Button(input_frame, text="Set Size", command=self.set_table_size, font=("Arial", 14), bg="#90ee90", fg="#000080")
        set_size_button.grid(row=0, column=2, padx=5, pady=5)

        key_label = tk.Label(input_frame, text="Key:", font=("Arial", 14), bg="#f0f8ff", fg="#000080")
        key_label.grid(row=1, column=0, padx=5, pady=5)
        self.key_entry = tk.Entry(input_frame, font=("Arial", 14))
        self.key_entry.grid(row=1, column=1, padx=5, pady=5)

        value_label = tk.Label(input_frame, text="Value:", font=("Arial", 14), bg="#f0f8ff", fg="#000080")
        value_label.grid(row=2, column=0, padx=5, pady=5)
        self.value_entry = tk.Entry(input_frame, font=("Arial", 14))
        self.value_entry.grid(row=2, column=1, padx=5, pady=5)

        button_frame = tk.Frame(self.root, bg="#f0f8ff")
        button_frame.pack(pady=10)

        insert_btn = tk.Button(button_frame, text="Insert", command=self.insert_value, font=("Arial", 14), bg="#90ee90", fg="#000080")
        insert_btn.grid(row=0, column=0, padx=5, pady=5)

        delete_btn = tk.Button(button_frame, text="Delete", command=self.delete_value, font=("Arial", 14), bg="#ffcccb", fg="#000080")
        delete_btn.grid(row=0, column=1, padx=5, pady=5)

        search_btn = tk.Button(button_frame, text="Search", command=self.search_value, font=("Arial", 14), bg="#ffd700", fg="#000080")
        search_btn.grid(row=0, column=2, padx=5, pady=5)

        traverse_btn = tk.Button(button_frame, text="Traverse", command=self.traverse_table, font=("Arial", 14), bg="#add8e6", fg="#000080")
        traverse_btn.grid(row=0, column=3, padx=5, pady=5)

        quit_btn = tk.Button(button_frame, text="Quit", command=self.root.quit, font=("Arial", 14), bg="#ff4500", fg="#ffffff")
        quit_btn.grid(row=0, column=4, padx=5, pady=5)

        self.output_frame = tk.Frame(self.root, bg="#f0f8ff")
        self.output_frame.pack(pady=10)

        self.output_text = tk.Text(self.output_frame, height=10, width=60, font=("Arial", 12))
        self.output_text.pack()

    def set_table_size(self):
        size = self.size_entry.get()
        if size.isdigit():
            self.hash_table = HashTable(int(size))
            messagebox.showinfo("Info", f"Hash table of size {size} created.")
        else:
            messagebox.showwarning("Warning", "Please enter a valid size.")

    def insert_value(self):
        if self.hash_table:
            key = self.key_entry.get()
            value = self.value_entry.get()
            if key.isdigit():
                self.hash_table.insert(int(key), value)
                messagebox.showinfo("Info", f"Inserted key {key} with value {value}.")
            else:
                messagebox.showwarning("Warning", "Key must be an integer.")
        else:
            messagebox.showwarning("Warning", "Please set the table size first.")

    def delete_value(self):
        if self.hash_table:
            key = self.key_entry.get()
            if key.isdigit():
                self.hash_table.delete(int(key))
                messagebox.showinfo("Info", f"Deleted key {key}.")
            else:
                messagebox.showwarning("Warning", "Key must be an integer.")
        else:
            messagebox.showwarning("Warning", "Please set the table size first.")

    def search_value(self):
        if self.hash_table:
            key = self.key_entry.get()
            if key.isdigit():
                value = self.hash_table.search(int(key))
                if value is not None:
                    messagebox.showinfo("Info", f"Found value: {value} for key {key}.")
                else:
                    messagebox.showinfo("Info", f"Key {key} not found.")
            else:
                messagebox.showwarning("Warning", "Key must be an integer.")
        else:
            messagebox.showwarning("Warning", "Please set the table size first.")

    def traverse_table(self):
        if self.hash_table:
            elements = self.hash_table.traverse()
            self.output_text.delete(1.0, tk.END)
            if elements:
                self.output_text.insert(tk.END, "\n".join(elements))
            else:
                self.output_text.insert(tk.END, "Hash table is empty.")
        else:
            messagebox.showwarning("Warning", "Please set the table size first.")

if __name__ == "__main__":
    root = tk.Tk()
    app = HashTableApp(root)
    root.mainloop()
