#External padding, horizontally
import tkinter as tk
root = tk.Tk()
w = tk.Label(root, text="Red Sun", bg="red", fg="white")
w.pack(fill=tk.X, padx=10)
w = tk.Label(root, text="Green Grass", bg="green", fg="black")
w.pack(fill=tk.X, padx=10)
w = tk.Label(root, text="Blue Sky", bg="blue", fg="white")
w.pack(fill=tk.X, padx=10)
tk.mainloop()