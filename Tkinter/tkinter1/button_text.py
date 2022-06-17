import tkinter as tk
def write_slogan():
    print("Python is Easy to Learn as Compare to any Language!")
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
button = tk.Button(frame,text = "QUIT",fg="red",command=quit)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,text="Hello",command=write_slogan).pack(side=tk.LEFT)
root.mainloop()
