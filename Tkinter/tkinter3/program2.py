from tkinter import *
master = Tk()
w = Canvas(master, width=200, height=100)
w.pack()
w.create_rectangle(50, 20, 150, 80, fill="#476042") #create a Rectangle
w.create_rectangle(65, 35, 135, 65, fill="yellow") #Create a Inner Rectangle
w.create_line(0, 0, 50, 20, fill="#476042", width=3) # Create Left Up-Line
w.create_line(0, 100, 50, 80, fill="#476042", width=3) # Create Left Down-Line
w.create_line(150,20, 200, 0, fill="#476042", width=3) # Create Right Up-Line
w.create_line(150, 80, 200, 100, fill="#476042", width=3) # Create Right Down-Line
mainloop ()
