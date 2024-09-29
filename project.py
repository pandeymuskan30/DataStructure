import tkinter as tk
import os

# Create the main window
root = tk.Tk()
root.title("12 Different Buttons")
root.geometry('800x600')
root.configure(bg="#8FBC8F")  # Set a light gray background for the main window

# Add a heading label at the top
heading = tk.Label(root, text="Data Structures", font=("Helvetica", 16), bg="#f0f0f0", fg="#333")
heading.grid(row=0, column=0, columnspan=4, pady=10)

# Text area for displaying information
info_text = tk.Text(root, height=15, width=90, wrap=tk.WORD, bg="#fff", fg="#000", font=("Helvetica", 12))
info_text.grid(row=5, column=0, columnspan=4, padx=10, pady=10)

# Function to display information about the data structure
def show_info(button_label):
    info = scripts.get(button_label, ("", ""))[1]
    info_text.delete(1.0, tk.END)  # Clear previous information
    info_text.insert(tk.END, info)  # Insert new information

# Function to handle button clicks
def button_click(button_label):
    script_to_run, _ = scripts.get(button_label, (None, None))
    if script_to_run:
        os.system(f'python {script_to_run}')

# Map each button label to its corresponding script and information
scripts = {
    "Abstract Data Types (ADT)": (
        "prac1.py", 
        "Abstract Data Types (ADT) are theoretical models that define data types purely by their behavior. "
        "They are characterized by their operations and the way data is stored, rather than how it is implemented."
    ),
    "Stack": (
        "stack.py", 
        "A Stack is a linear data structure that follows a Last In First Out (LIFO) order. "
        "Elements can only be added or removed from the top of the stack. Common operations include Push (add) and Pop (remove)."
    ),
    "Singly Linked List": (
        "singly_linked_list.py", 
        "A Singly Linked List is a collection of nodes where each node contains data and a reference to the next node. "
        "This structure allows for efficient insertions and deletions but requires traversal to access elements."
    ),
    "Doubly Linked List": (
        "doubly_linked_list.py", 
        "A Doubly Linked List consists of nodes where each node has references to both the next and previous nodes. "
        "This allows for bidirectional traversal, making insertions and deletions easier at both ends."
    ),
    "Queues": (
        "Quenegui.py", 
        "A Queue is a linear structure that follows a First In First Out (FIFO) order. "
        "Elements are added at the back and removed from the front, making it ideal for scheduling tasks."
    ),
    "Priority Queues": (
        "Priorityquenegui.py", 
        "A Priority Queue is an abstract data type where each element has a priority. "
        "Elements with higher priority are served before those with lower priority, regardless of their order in the queue."
    ),
    "Binary Tree": (
        "binary_tree.py", 
        "A Binary Tree is a hierarchical structure in which each node has at most two children. "
        "It is used for efficient searching and sorting, and has various types including full, complete, and balanced trees."
    ),
    "Huffman Coding": (
        "huffman_coding.py", 
        "Huffman Coding is a compression algorithm that assigns variable-length codes to input characters based on their frequencies. "
        "It is widely used in data compression techniques, such as in ZIP files."
    ),
    "Graph": (
        "graph.py", 
        "A Graph is a collection of vertices connected by edges. Graphs can be directed or undirected, and weighted or unweighted. "
        "They are used to represent networks, such as social connections or transportation systems."
    ),
    "Travelling Salesman Problem": (
        "tsp.py", 
        "The Travelling Salesman Problem (TSP) is an optimization problem that seeks the shortest possible route that visits a set of locations and returns to the origin. "
        "It is NP-hard, meaning there is no known efficient solution."
    ),
    "Hash Table (with no collisions)": (
        "hash_table.py", 
        "A Hash Table is a data structure that maps keys to values for efficient lookup. It uses a hash function to compute an index into an array of buckets or slots. "
        "With no collisions, each key maps to a unique index, allowing for constant time complexity for searches."
    ),
    "Hashing": (
        "hashing.py", 
        "Hashing is the process of converting input data of arbitrary size into a fixed-size value. "
        "Hash functions are used in data structures like hash tables to ensure efficient data retrieval and storage."
    )
}

# List of different button labels
button_labels = [
    "Abstract Data Types (ADT)", "Stack", "Singly Linked List", "Doubly Linked List",
    "Queues", "Priority Queues", "Binary Tree", "Huffman Coding",
    "Graph", "Travelling Salesman Problem", "Hash Table (with no collisions)", "Hashing"
]

# Create and place buttons with information on hover
for i, label in enumerate(button_labels):
    button = tk.Button(root, text=label, command=lambda label=label: button_click(label), 
                       width=25, font=("Helvetica", 12), bg="#8B8B83", fg="#fff")
    button.grid(row=(i // 4) + 1, column=i % 4, padx=40, pady=40)
    
    # Bind hover events to show info
    button.bind("<Enter>", lambda e, label=label: show_info(label))
    button.bind("<Leave>", lambda e: info_text.delete(1.0, tk.END))  # Clear info on leave

# Start the Tkinter event loop
root.mainloop()
