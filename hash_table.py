import tkinter as tk
from tkinter import messagebox

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
        self.table[index] = (key, value)

    def delete(self, key):
        """Delete the value associated with the given key."""
        index = self.hash_function(key)
        if self.table[index] and self.table[index][0] == key:
            self.table[index] = None

    def search(self, key):
        """Search for the value associated with the given key."""
        index = self.hash_function(key)
        if self.table[index] and self.table[index][0] == key:
            return self.table[index][1]
        return None

    def traverse(self):
        """Traverse and return all key-value pairs in the hash table."""
        items = []
        for index, item in enumerate(self.table):
            if item is not None:
                key, value = item
                items.append(f"Index {index}: Key {key}, Value {value}")
        return items

class HashTableApp:
    def __init__(self, master):
        self.master = master
        master.title("Hash Table GUI")
        master.configure(bg="#f0f8ff")  # Light blue background

        self.hash_table = HashTable(size=10)

        # Header label
        self.title_label = tk.Label(master, text="Application created by Muskan Pandey S098", font=("Arial", 14, "bold"), bg="#f0f8ff")
        self.title_label.pack(pady=10)

        # Create input fields
        self.key_label = tk.Label(master, text="Key:", bg="#f0f8ff", font=("Arial", 12))
        self.key_label.pack(pady=5)
        self.key_entry = tk.Entry(master, font=("Arial", 12))
        self.key_entry.pack(pady=5)

        self.value_label = tk.Label(master, text="Value:", bg="#f0f8ff", font=("Arial", 12))
        self.value_label.pack(pady=5)
        self.value_entry = tk.Entry(master, font=("Arial", 12))
        self.value_entry.pack(pady=5)

        # Create buttons
        self.insert_button = tk.Button(master, text="Insert", command=self.insert, bg="#90ee90", font=("Arial", 12))
        self.insert_button.pack(pady=5)

        self.search_button = tk.Button(master, text="Search", command=self.search, bg="#add8e6", font=("Arial", 12))
        self.search_button.pack(pady=5)

        self.delete_button = tk.Button(master, text="Delete", command=self.delete, bg="#ffcccb", font=("Arial", 12))
        self.delete_button.pack(pady=5)

        self.traverse_button = tk.Button(master, text="Traverse", command=self.traverse, bg="#ffd700", font=("Arial", 12))
        self.traverse_button.pack(pady=5)

        # Output text area
        self.output_text = tk.Text(master, height=10, width=50, font=("Arial", 12), bg="#ffffff")
        self.output_text.pack(pady=10)

    def insert(self):
        key = int(self.key_entry.get())
        value = self.value_entry.get()
        self.hash_table.insert(key, value)
        self.output_text.insert(tk.END, f"Inserted: Key {key}, Value {value}\n")
        self.key_entry.delete(0, tk.END)
        self.value_entry.delete(0, tk.END)

    def search(self):
        key = int(self.key_entry.get())
        value = self.hash_table.search(key)
        if value is not None:
            self.output_text.insert(tk.END, f"Found: Key {key}, Value {value}\n")
        else:
            self.output_text.insert(tk.END, f"Key {key} not found.\n")

    def delete(self):
        key = int(self.key_entry.get())
        self.hash_table.delete(key)
        self.output_text.insert(tk.END, f"Deleted: Key {key}\n")

    def traverse(self):
        items = self.hash_table.traverse()
        self.output_text.delete(1.0, tk.END)  # Clear the output text
        if items:
            self.output_text.insert(tk.END, "\n".join(items) + "\n")
        else:
            self.output_text.insert(tk.END, "Hash table is empty.\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = HashTableApp(root)
    root.mainloop()
