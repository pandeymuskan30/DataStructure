import tkinter as tk
from tkinter import messagebox

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, root, key):
        if key < root.val:
            if root.left is None:
                root.left = Node(key)
            else:
                self._insert(root.left, key)
        else:
            if root.right is None:
                root.right = Node(key)
            else:
                self._insert(root.right, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if root is None:
            return root
        if key < root.val:
            root.left = self._delete(root.left, key)
        elif key > root.val:
            root.right = self._delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            min_larger_node = self._get_min(root.right)
            root.val = min_larger_node.val
            root.right = self._delete(root.right, min_larger_node.val)
        return root

    def _get_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder_traversal(self):
        return self._inorder_traversal(self.root)

    def _inorder_traversal(self, root):
        res = []
        if root:
            res = self._inorder_traversal(root.left)
            res.append(root.val)
            res = res + self._inorder_traversal(root.right)
        return res

    def draw(self, canvas, x, y, dx):
        if self.root:
            self._draw_tree(canvas, self.root, x, y, dx)

    def _draw_tree(self, canvas, node, x, y, dx):
        if node is not None:
            # Draw the node
            canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill='lightblue')
            canvas.create_text(x, y, text=str(node.val))
            if node.left is not None:
                canvas.create_line(x, y, x - dx, y + 60)
                self._draw_tree(canvas, node.left, x - dx, y + 60, dx / 2)
            if node.right is not None:
                canvas.create_line(x, y, x + dx, y + 60)
                self._draw_tree(canvas, node.right, x + dx, y + 60, dx / 2)

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Binary Tree Application")

        # Heading
        heading_label = tk.Label(master, text="Binary Tree Application crated by Muskan Pandey", font=("Helvetica", 16, "bold"))
        heading_label.pack(pady=10)

        self.tree = BinaryTree()

        self.input_entry = tk.Entry(master)
        self.input_entry.pack()

        self.insert_button = tk.Button(master, text="Insert", command=self.insert)
        self.insert_button.pack()

        self.delete_button = tk.Button(master, text="Delete", command=self.delete)
        self.delete_button.pack()

        self.inorder_button = tk.Button(master, text="Inorder Traversal", command=self.show_inorder)
        self.inorder_button.pack()

        self.plot_button = tk.Button(master, text="Plot Tree", command=self.plot_tree)
        self.plot_button.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

        self.canvas = tk.Canvas(master, width=800, height=600, bg='white')
        self.canvas.pack()

        credits_label = tk.Label(master, text="Application developed by Muskan Pandey")
        credits_label.pack()

    def insert(self):
        try:
            key = int(self.input_entry.get())
            self.tree.insert(key)
            self.result_label.config(text=f"Inserted {key}")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid integer.")

    def delete(self):
        try:
            key = int(self.input_entry.get())
            self.tree.delete(key)
            self.result_label.config(text=f"Deleted {key}")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid integer.")

    def show_inorder(self):
        result = self.tree.inorder_traversal()
        self.result_label.config(text="Inorder: " + ', '.join(map(str, result)))

    def plot_tree(self):
        self.canvas.delete("all")  # Clear the canvas before drawing
        self.tree.draw(self.canvas, 400, 20, 200)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
