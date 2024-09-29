import tkinter as tk
from tkinter import messagebox
import math

class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
            return f"Vertex {vertex} added."
        else:
            return f"Vertex {vertex} already exists."

    def remove_vertex(self, vertex):
        if vertex in self.graph:
            for adjacent in list(self.graph[vertex]):
                self.graph[adjacent].remove(vertex)
            del self.graph[vertex]
            return f"Vertex {vertex} removed."
        else:
            return f"Vertex {vertex} does not exist."

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            if vertex2 not in self.graph[vertex1]:
                self.graph[vertex1].append(vertex2)
            if vertex1 not in self.graph[vertex2]:
                self.graph[vertex2].append(vertex1)
            return f"Edge added between {vertex1} and {vertex2}."
        else:
            return "One or both vertices not found."

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            if vertex2 in self.graph[vertex1]:
                self.graph[vertex1].remove(vertex2)
            if vertex1 in self.graph[vertex2]:
                self.graph[vertex2].remove(vertex1)
            return f"Edge removed between {vertex1} and {vertex2}."
        else:
            return "One or both vertices not found."

    def display(self):
        return '\n'.join(f"{vertex}: {edges}" for vertex, edges in self.graph.items())

class GraphGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Graph GUI")
        self.graph = Graph()

        # Set the initial window size and minimum size
        self.root.geometry("800x600")
        self.root.minsize(800, 600)

        # Create and place widgets
        self.create_widgets()

    def create_widgets(self):
        # Application Name Label at the top
        self.title_label = tk.Label(self.root, text="Graph GUI Application by Muskan Pandey S098", font=("Arial", 16, "bold"))
        self.title_label.pack(side=tk.TOP, fill=tk.X, pady=10)

        # Create a frame for the controls
        control_frame = tk.Frame(self.root)
        control_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        # Vertex Entry
        tk.Label(control_frame, text="Vertex:", font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=5)
        self.vertex_entry = tk.Entry(control_frame, font=("Arial", 12))
        self.vertex_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        # Add Vertex Button
        self.add_vertex_button = tk.Button(control_frame, text="Add Vertex", command=self.add_vertex, font=("Arial", 12))
        self.add_vertex_button.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        # Remove Vertex Button
        self.remove_vertex_button = tk.Button(control_frame, text="Remove Vertex", command=self.remove_vertex, font=("Arial", 12))
        self.remove_vertex_button.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

        # Edge Vertex 1 Entry
        tk.Label(control_frame, text="Vertex 1:", font=("Arial", 12)).grid(row=3, column=0, padx=5, pady=5)
        self.edge_vertex1_entry = tk.Entry(control_frame, font=("Arial", 12))
        self.edge_vertex1_entry.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

        # Edge Vertex 2 Entry
        tk.Label(control_frame, text="Vertex 2:", font=("Arial", 12)).grid(row=4, column=0, padx=5, pady=5)
        self.edge_vertex2_entry = tk.Entry(control_frame, font=("Arial", 12))
        self.edge_vertex2_entry.grid(row=4, column=1, padx=5, pady=5, sticky="ew")

        # Add Edge Button
        self.add_edge_button = tk.Button(control_frame, text="Add Edge", command=self.add_edge, font=("Arial", 12))
        self.add_edge_button.grid(row=5, column=1, padx=5, pady=5, sticky="ew")

        # Remove Edge Button
        self.remove_edge_button = tk.Button(control_frame, text="Remove Edge", command=self.remove_edge, font=("Arial", 12))
        self.remove_edge_button.grid(row=6, column=1, padx=5, pady=5, sticky="ew")

        # Output Text Area
        self.output_text = tk.Text(self.root, height=10, width=50, font=("Arial", 12))
        self.output_text.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Graph Canvas
        self.graph_canvas = tk.Canvas(self.root, bg='white', width=600, height=400)
        self.graph_canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Application Creator Label
        self.creator_label = tk.Label(self.root, text="Application created by Muskan Pandey S098", font=("Arial", 12))
        self.creator_label.pack(side=tk.BOTTOM, pady=10)

    def add_vertex(self):
        vertex = self.vertex_entry.get().strip()
        if vertex:
            result = self.graph.add_vertex(vertex)
            self.display_result(result)
            self.draw_graph()
        else:
            messagebox.showwarning("Input Error", "Vertex cannot be empty.")
        self.vertex_entry.delete(0, tk.END)

    def remove_vertex(self):
        vertex = self.vertex_entry.get().strip()
        if vertex:
            result = self.graph.remove_vertex(vertex)
            self.display_result(result)
            self.draw_graph()
        else:
            messagebox.showwarning("Input Error", "Vertex cannot be empty.")
        self.vertex_entry.delete(0, tk.END)

    def add_edge(self):
        vertex1 = self.edge_vertex1_entry.get().strip()
        vertex2 = self.edge_vertex2_entry.get().strip()
        if vertex1 and vertex2:
            result = self.graph.add_edge(vertex1, vertex2)
            self.display_result(result)
            self.draw_graph()
        else:
            messagebox.showwarning("Input Error", "Both vertices must be provided.")
        self.edge_vertex1_entry.delete(0, tk.END)
        self.edge_vertex2_entry.delete(0, tk.END)

    def remove_edge(self):
        vertex1 = self.edge_vertex1_entry.get().strip()
        vertex2 = self.edge_vertex2_entry.get().strip()
        if vertex1 and vertex2:
            result = self.graph.remove_edge(vertex1, vertex2)
            self.display_result(result)
            self.draw_graph()
        else:
            messagebox.showwarning("Input Error", "Both vertices must be provided.")
        self.edge_vertex1_entry.delete(0, tk.END)
        self.edge_vertex2_entry.delete(0, tk.END)

    def display_result(self, message):
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, message + "\n")
        self.display_graph()

    def display_graph(self):
        self.output_text.insert(tk.END, "\nGraph:\n" + self.graph.display())

    def draw_graph(self):
        self.graph_canvas.delete("all")  # Clear the canvas
        vertex_positions = {}
        width = self.graph_canvas.winfo_width()
        height = self.graph_canvas.winfo_height()
        num_vertices = len(self.graph.graph)

        # Determine positions for each vertex in a circular layout
        angle_increment = 360 / num_vertices if num_vertices > 0 else 1
        radius = min(width, height) / 3 - 20  # Adjust radius for better visibility

        for i, vertex in enumerate(self.graph.graph.keys()):
            angle = i * angle_increment
            x = width / 2 + radius * math.cos(math.radians(angle))
            y = height / 2 + radius * math.sin(math.radians(angle))
            vertex_positions[vertex] = (x, y)
            self.graph_canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill='lightblue')
            self.graph_canvas.create_text(x, y, text=vertex)

        # Draw edges
        for vertex, edges in self.graph.graph.items():
            x1, y1 = vertex_positions[vertex]
            for edge in edges:
                x2, y2 = vertex_positions[edge]
                self.graph_canvas.create_line(x1, y1, x2, y2)

# Run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = GraphGUI(root)
    root.mainloop()
