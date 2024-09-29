import tkinter as tk
from itertools import permutations
import math

class TSP:
    def __init__(self, distance_matrix):
        self.distance_matrix = distance_matrix
        self.num_cities = len(distance_matrix)

    def calculate_total_distance(self, route):
        """Calculate the total distance of a given route."""
        total_distance = 0
        for i in range(len(route) - 1):
            total_distance += self.distance_matrix[route[i]][route[i + 1]]
        total_distance += self.distance_matrix[route[-1]][route[0]]  # Return to starting city
        return total_distance

    def solve(self):
        """Solve the TSP using brute force."""
        min_distance = math.inf
        best_route = None
        for perm in permutations(range(self.num_cities)):
            current_distance = self.calculate_total_distance(perm)
            if current_distance < min_distance:
                min_distance = current_distance
                best_route = perm
        return best_route, min_distance

class TSPApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Traveling Salesman Problem Solver")

        self.city_count = 4  # Number of cities
        self.distance_matrix = [[0] * self.city_count for _ in range(self.city_count)]
        self.city_coordinates = [
            (100, 100),  # City 0
            (200, 50),   # City 1
            (300, 150),  # City 2
            (400, 100)   # City 3
        ]

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Enter Distance Matrix (comma-separated):").pack(pady=10)

        self.matrix_text = tk.Text(self.root, height=5, width=50)
        self.matrix_text.pack(pady=10)

        self.solve_button = tk.Button(self.root, text="Solve TSP", command=self.solve_tsp)
        self.solve_button.pack(pady=10)

        self.result_text = tk.Text(self.root, height=10, width=50)
        self.result_text.pack(pady=10)

        self.canvas = tk.Canvas(self.root, width=500, height=300, bg='white')
        self.canvas.pack(pady=10)

    def solve_tsp(self):
        try:
            # Get the distance matrix from the user input
            input_text = self.matrix_text.get("1.0", tk.END).strip()
            rows = input_text.split("\n")
            self.distance_matrix = [list(map(int, row.split(","))) for row in rows]

            # Validate the distance matrix
            if len(self.distance_matrix) != len(self.distance_matrix[0]):
                raise ValueError("Distance matrix must be square.")

            tsp = TSP(self.distance_matrix)
            best_route, min_distance = tsp.solve()
            self.display_result(best_route, min_distance)
            self.plot_route(best_route)
        except Exception as e:
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, f"Error: {str(e)}\n")

    def display_result(self, route, distance):
        route_str = " -> ".join(f"City {city}" for city in route)
        result = f"Optimal Route: {route_str}\nTotal Distance: {distance}\n"
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, result)

    def plot_route(self, route):
        self.canvas.delete("all")  # Clear previous drawings

        # Draw the cities
        for i, (x, y) in enumerate(self.city_coordinates):
            self.canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill='blue')  # City points
            self.canvas.create_text(x, y - 10, text=f'City {i}', anchor='s')

        # Draw the optimal route
        for i in range(len(route)):
            start_city = self.city_coordinates[route[i]]
            end_city = self.city_coordinates[route[(i + 1) % len(route)]]
            self.canvas.create_line(start_city[0], start_city[1], end_city[0], end_city[1], fill='red', width=2)

if __name__ == "__main__":
    root = tk.Tk()
    app = TSPApp(root)
    root.mainloop()
