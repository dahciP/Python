import tkinter as tk
root = tk.Tk()
v = tk.IntVar()
tk.Label(root,text="""Choose a Programing Language""",justify = tk.LEFT,padx = 20).pack()
tk.Radiobutton(root,text="Python",padx=20,variable=v,value=1).pack(anchor=tk.W)
tk.Radiobutton(root,text="Perl",padx=20,variable=v,value=2).pack(anchor=tk.W)
tk.Radiobutton(root,text="C,C++",padx=20,variable=v,value=3).pack(anchor=tk.W)
tk.Radiobutton(root,text="Java",padx=20,variable=v,value=4).pack(anchor=tk.W)
tk.Radiobutton(root,text=".net",padx=20,variable=v,value=5).pack(anchor=tk.W)
tk.Radiobutton(root,text="PHP",padx=20,variable=v,value=6).pack(anchor=tk.W)
tk.Radiobutton(root,text="React",padx=20,variable=v,value=7).pack(anchor=tk.W)
root.mainloop()