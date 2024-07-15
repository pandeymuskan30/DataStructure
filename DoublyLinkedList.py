import tkinter as tk
from tkinter import messagebox

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        n = Node(data)
        if self.head is None:
            self.head = n
        else:
            temp = self.head
            temp.prev = n
            n.next = temp
            self.head = n

    def insert_at_ending(self, data):
        n = Node(data)
        if self.head is None:
            self.head = n
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = n
            n.prev = current

    def insert_at_position(self, data, position):
        if position < 0:
            return "Position should be greater than or equal to 0"

        n = Node(data)
        if position == 0:
            self.insert_at_beginning(data)
            return

        current = self.head
        for _ in range(position - 1):
            if current is None:
                break
            current = current.next

        if current is None or current.next is None:
            self.insert_at_ending(data)
        else:
            n.next = current.next
            n.prev = current
            current.next.prev = n
            current.next = n

    def delete_at_beginning(self):
        if self.head is None:
            return "List is empty, nothing to delete"
        current = self.head
        self.head = current.next
        if self.head:
            self.head.prev = None
        current.next = None

    def delete_at_ending(self):
        if self.head is None:
            return "List is empty, nothing to delete"
        if self.head.next is None:
            self.head = None
            return
        before = self.head
        temp = self.head.next
        while temp.next is not None:
            temp = temp.next
            before = before.next
        before.next = None
        temp.prev = None

    def delete_at_position(self, position):
        if self.head is None:
            return "List is empty, nothing to delete"
        if position < 0:
            return "Position should be greater than or equal to 0"
        if position == 0:
            self.delete_at_beginning()
            return

        current = self.head
        before = None
        for _ in range(position):
            before = current
            current = current.next
            if current is None:
                return "Position is out of bounds"

        if current.next is not None:
            current.next.prev = before
        if before is not None:
            before.next = current.next
        current.next = None
        current.prev = None

    def display(self):
        if self.head is None:
            return "List is empty"
        else:
            elements = []
            current = self.head
            while current is not None:
                elements.append(str(current.data))
                current = current.next
            return " <-> ".join(elements)

class DoubleLinkedListApp:
    def __init__(self, root):
        self.linked_list = DoubleLinkedList()
        self.root = root
        self.root.title("Doubly Linked List GUI")

        self.data_label = tk.Label(root, text="Data:")
        self.data_label.pack()
        self.data_entry = tk.Entry(root)
        self.data_entry.pack()

        self.position_label = tk.Label(root, text="Position (for insert/delete at position):")
        self.position_label.pack()
        self.position_entry = tk.Entry(root)
        self.position_entry.pack()

        self.insert_beg_btn = tk.Button(root, text="Insert at Beginning", command=self.insert_at_beginning)
        self.insert_beg_btn.pack()

        self.insert_end_btn = tk.Button(root, text="Insert at End", command=self.insert_at_ending)
        self.insert_end_btn.pack()

        self.insert_pos_btn = tk.Button(root, text="Insert at Position", command=self.insert_at_position)
        self.insert_pos_btn.pack()

        self.del_beg_btn = tk.Button(root, text="Delete at Beginning", command=self.delete_at_beginning)
        self.del_beg_btn.pack()

        self.del_end_btn = tk.Button(root, text="Delete at End", command=self.delete_at_ending)
        self.del_end_btn.pack()

        self.del_pos_btn = tk.Button(root, text="Delete at Position", command=self.delete_at_position)
        self.del_pos_btn.pack()

        self.traverse_btn = tk.Button(root, text="Traverse", command=self.traverse)
        self.traverse_btn.pack()

        self.output_label = tk.Label(root, text="")
        self.output_label.pack()

    def insert_at_beginning(self):
        data = self.data_entry.get()
        if data:
            self.linked_list.insert_at_beginning(data)
            self.data_entry.delete(0, tk.END)
            self.display_list()

    def insert_at_ending(self):
        data = self.data_entry.get()
        if data:
            self.linked_list.insert_at_ending(data)
            self.data_entry.delete(0, tk.END)
            self.display_list()

    def insert_at_position(self):
        data = self.data_entry.get()
        position = self.position_entry.get()
        if data and position.isdigit():
            self.linked_list.insert_at_position(data, int(position))
            self.data_entry.delete(0, tk.END)
            self.position_entry.delete(0, tk.END)
            self.display_list()

    def delete_at_beginning(self):
        result = self.linked_list.delete_at_beginning()
        if result:
            messagebox.showinfo("Info", result)
        self.display_list()

    def delete_at_ending(self):
        result = self.linked_list.delete_at_ending()
        if result:
            messagebox.showinfo("Info", result)
        self.display_list()

    def delete_at_position(self):
        position = self.position_entry.get()
        if position.isdigit():
            result = self.linked_list.delete_at_position(int(position))
            if result:
                messagebox.showinfo("Info", result)
            self.position_entry.delete(0, tk.END)
            self.display_list()

    def traverse(self):
        elements = self.linked_list.display()
        messagebox.showinfo("Doubly Linked List", elements)

    def display_list(self):
        elements = self.linked_list.display()
        self.output_label.config(text=elements)

if __name__ == "__main__":
    root = tk.Tk()
    app = DoubleLinkedListApp(root)
    root.mainloop()
