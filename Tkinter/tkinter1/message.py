import tkinter as tk
master = tk.Tk()
sm = "Welcome to SM INFOTECH Python Program.\n\n\n(By SM Classes)"
msg = tk.Message(master, text = sm)
msg.config(bg='lightgreen',font=('times',24,'italic'))
msg.pack()
tk.mainloop()