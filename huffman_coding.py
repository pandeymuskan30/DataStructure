import tkinter as tk
from tkinter import messagebox, scrolledtext
import heapq
from collections import Counter

class Node:
    def __init__(self, char=None, freq=None):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(frequencies):
    heap = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(freq=left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]

def generate_codes(node, prefix="", codebook={}):
    if node:
        if node.char is not None:
            codebook[node.char] = prefix
        generate_codes(node.left, prefix + "0", codebook)
        generate_codes(node.right, prefix + "1", codebook)
    return codebook

def huffman_encoding(data):
    if not data:
        return "", {}

    frequencies = Counter(data)
    root = build_huffman_tree(frequencies)
    codebook = generate_codes(root)
    encoded_data = ''.join(codebook[char] for char in data)

    return encoded_data, codebook, root

def huffman_decoding(encoded_data, codebook):
    reverse_codebook = {v: k for k, v in codebook.items()}
    decoded_data = ""
    current_code = ""

    for bit in encoded_data:
        current_code += bit
        if current_code in reverse_codebook:
            decoded_data += reverse_codebook[current_code]
            current_code = ""

    return decoded_data

class HuffmanCodingApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Huffman Coding Application")
        
        self.hading_label = tk.Label(master, text="Application created by Muskan Pandey")
        self.hading_label.pack()

        self.input_label = tk.Label(master, text="Enter text:")
        self.input_label.pack()

        self.input_text = tk.Entry(master, width=50)
        self.input_text.pack()

        self.encode_button = tk.Button(master, text="Encode", command=self.encode)
        self.encode_button.pack()

        self.encoded_label = tk.Label(master, text="Encoded Data:")
        self.encoded_label.pack()

        self.encoded_text = scrolledtext.ScrolledText(master, width=50, height=6)
        self.encoded_text.pack()

        self.codebook_label = tk.Label(master, text="Codebook:")
        self.codebook_label.pack()

        self.codebook_text = scrolledtext.ScrolledText(master, width=50, height=8)
        self.codebook_text.pack()

        self.decode_button = tk.Button(master, text="Decode", command=self.decode)
        self.decode_button.pack()

        self.decoded_label = tk.Label(master, text="Decoded Data:")
        self.decoded_label.pack()

        self.decoded_text = scrolledtext.ScrolledText(master, width=50, height=6)
        self.decoded_text.pack()

        self.tree_canvas = tk.Canvas(master, width=800, height=400, bg='white')
        self.tree_canvas.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

    def encode(self):
        data = self.input_text.get()
        if not data:
            messagebox.showerror("Input Error", "Please enter some text to encode.")
            return
        
        encoded_data, codebook, root = huffman_encoding(data)
        self.encoded_text.delete(1.0, tk.END)
        self.encoded_text.insert(tk.END, encoded_data)
        
        self.codebook_text.delete(1.0, tk.END)
        for char, code in codebook.items():
            self.codebook_text.insert(tk.END, f"{char}: {code}\n")
        
        self.result_label.config(text="Encoding complete!")

        # Save the encoded data and codebook for decoding
        self.encoded_data = encoded_data
        self.codebook = codebook

        # Draw Huffman Tree
        self.draw_huffman_tree(root)

    def decode(self):
        if hasattr(self, 'encoded_data') and hasattr(self, 'codebook'):
            decoded_data = huffman_decoding(self.encoded_data, self.codebook)
            self.decoded_text.delete(1.0, tk.END)
            self.decoded_text.insert(tk.END, decoded_data)
            self.result_label.config(text="Decoding complete!")
        else:
            messagebox.showerror("Decode Error", "Please encode some text first.")

    def draw_huffman_tree(self, node, x=400, y=20, dx=200):
        if node is not None:
            # Draw the node
            if node.char is not None:
                self.tree_canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill='lightblue')
                self.tree_canvas.create_text(x, y, text=node.char)
            else:
                self.tree_canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill='lightgreen')
                self.tree_canvas.create_text(x, y, text=f"{node.freq}")

            if node.left is not None:
                self.tree_canvas.create_line(x, y, x - dx, y + 60)
                self.draw_huffman_tree(node.left, x - dx, y + 60, dx / 2)
            if node.right is not None:
                self.tree_canvas.create_line(x, y, x + dx, y + 60)
                self.draw_huffman_tree(node.right, x + dx, y + 60, dx / 2)

if __name__ == "__main__":
    root = tk.Tk()
    app = HuffmanCodingApp(root)
    root.mainloop()
