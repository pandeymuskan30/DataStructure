import tkinter as tk
from tkinter import messagebox, font

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_at_position(self, data, position):
        if position < 0:
            return "Invalid position!"
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(position - 1):
            if current is None:
                return "Position out of bounds!"
            current = current.next
        if current is None:
            return "Position out of bounds!"
        new_node.next = current.next
        current.next = new_node

    def delete_at_beginning(self):
        if self.is_empty():
            return None
        deleted_node = self.head
        self.head = self.head.next
        return deleted_node.data

    def delete_at_end(self):
        if self.is_empty():
            return None
        if self.head.next is None:
            deleted_node = self.head
            self.head = None
            return deleted_node.data
        current = self.head
        while current.next.next:
            current = current.next
        deleted_node = current.next
        current.next = None
        return deleted_node.data

    def delete_node(self, key):
        current = self.head
        if current and current.data == key:
            self.head = current.next
            return
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        if current is None:
            return "Node not found!"
        prev.next = current.next

    def traverse(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

class LinkedListApp:
    def __init__(self, root):
        self.linked_list = LinkedList()
        self.root = root
        self.root.title("Linked List GUI")
        self.root.configure(bg="#F0F0F0")
        self.root.geometry("600x500")

        # Set font styles
        self.label_font = font.Font(family="Arial", size=15, weight="bold")
        self.button_font = font.Font(family="Arial", size=12)

        # Operation Frame
        self.operation_frame = tk.Frame(root, bg='lightblue')
        self.operation_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        # Result Frame
        self.result_frame = tk.Frame(root, bg='lightgray')
        self.result_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Title Label
        self.title_label = tk.Label(self.operation_frame, text="Linked List Operations", font=self.label_font, bg='lightblue')
        self.title_label.pack(pady=10)

        # Data Entry
        self.data_label = tk.Label(self.operation_frame, text="Data:", bg='lightblue', font=self.button_font)
        self.data_label.pack(pady=5)
        self.data_entry = tk.Entry(self.operation_frame, width=30, font=self.button_font)
        self.data_entry.pack(pady=5)

        # Position Entry
        self.position_label = tk.Label(self.operation_frame, text="Position (for insert):", bg='lightblue', font=self.button_font)
        self.position_label.pack(pady=5)
        self.position_entry = tk.Entry(self.operation_frame, width=10, font=self.button_font)
        self.position_entry.pack(pady=5)

        # Buttons
        self.insert_beg_btn = tk.Button(self.operation_frame, text="Insert at Beginning", command=self.insert_at_beginning, font=self.button_font)
        self.insert_beg_btn.pack(pady=5)

        self.insert_end_btn = tk.Button(self.operation_frame, text="Insert at End", command=self.insert_at_end, font=self.button_font)
        self.insert_end_btn.pack(pady=5)

        self.insert_pos_btn = tk.Button(self.operation_frame, text="Insert at Position", command=self.insert_at_position, font=self.button_font)
        self.insert_pos_btn.pack(pady=5)

        self.del_beg_btn = tk.Button(self.operation_frame, text="Delete at Beginning", command=self.delete_at_beginning, font=self.button_font)
        self.del_beg_btn.pack(pady=5)

        self.del_end_btn = tk.Button(self.operation_frame, text="Delete at End", command=self.delete_at_end, font=self.button_font)
        self.del_end_btn.pack(pady=5)

        self.del_node_btn = tk.Button(self.operation_frame, text="Delete Node", command=self.delete_node, font=self.button_font)
        self.del_node_btn.pack(pady=5)

        self.traverse_btn = tk.Button(self.operation_frame, text="Traverse", command=self.traverse, font=self.button_font)
        self.traverse_btn.pack(pady=5)

        # Output Label
        self.output_label = tk.Label(self.result_frame, text="", font=self.button_font)
        self.output_label.pack(pady=10)

        self.display_list()  # Initial display

    def insert_at_beginning(self):
        data = self.data_entry.get()
        if data:
            self.linked_list.insert_at_beginning(data)
            self.data_entry.delete(0, tk.END)
            self.display_list()

    def insert_at_end(self):
        data = self.data_entry.get()
        if data:
            self.linked_list.insert_at_end(data)
            self.data_entry.delete(0, tk.END)
            self.display_list()

    def insert_at_position(self):
        data = self.data_entry.get()
        position = self.position_entry.get()
        if data and position.isdigit():
            result = self.linked_list.insert_at_position(data, int(position))
            if result:
                messagebox.showerror("Error", result)
            self.data_entry.delete(0, tk.END)
            self.position_entry.delete(0, tk.END)
            self.display_list()

    def delete_at_beginning(self):
        data = self.linked_list.delete_at_beginning()
        if data is not None:
            messagebox.showinfo("Deleted", f"Deleted: {data}")
            self.display_list()

    def delete_at_end(self):
        data = self.linked_list.delete_at_end()
        if data is not None:
            messagebox.showinfo("Deleted", f"Deleted: {data}")
            self.display_list()

    def delete_node(self):
        data = self.data_entry.get()
        if data:
            result = self.linked_list.delete_node(data)
            if result:
                messagebox.showerror("Error", result)
            self.data_entry.delete(0, tk.END)
            self.display_list()

    def traverse(self):
        elements = self.linked_list.traverse()
        messagebox.showinfo("Linked List", " -> ".join(elements) + " -> None")

    def display_list(self):
        elements = self.linked_list.traverse()
        self.output_label.config(text="Linked List: " + " -> ".join(elements) + " -> None" if elements else "Linked List is empty.")

if __name__ == "__main__":
    root = tk.Tk()
    app = LinkedListApp(root)
    root.mainloop()
