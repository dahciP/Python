from tkinter import *

def calculate():
	num = int(entry.get())
	ele=' Table of ' + str(num) + '\n\n'
	for i in range(1,11):
		ele = ele + " " + str(num) + " x " + str(i) + " = " + str(num*i) + "\n"
	output_label.configure(text = ele, justify=CENTER)
	
main_window = Tk()
message_label = Label(text= ' Enter a number to \ndisplay its Table ' ,font=( ' Verdana ' , 12))
output_label = Label(font=( ' Times New Roman ' , 12))
entry = Entry(font=( ' Times New Roman ' , 12), width=6, justify=CENTER)
calc_button = Button(text= ' Show Multiplication Table ' , font=( ' Times New Roman ', 12), command=calculate)
message_label.grid(row=0, column=0,padx=10, pady=10)
entry.grid(row=0, column=1,padx=10, pady=10, ipady=10)
calc_button.grid(row=0, column=2,padx=10, pady=10)
output_label.grid(row=1, column=0, columnspan=3,padx=10, pady=10)
mainloop()
