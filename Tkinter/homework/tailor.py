from tkinter import *

def var_status():
    output.set("Anarkali Suit: %d,\nSuits with pants: %d,\nSalwar Suit: %d,\nDesigner Kurti: %d,\nJumpsuit: %d,\nGowns: %d" % (var1.get(), var2.get(), var3.get(), var4.get(), var5.get(), var6.get()))

def calculate():
        
    selected=list()
    if var1.get():
        selected.append(3200)
    if var2.get():
        selected.append(1550)
    if var3.get():
        selected.append(1500)
    if var4.get():
        selected.append(1200)
    if var5.get():
        selected.append(1800)
    if var6.get():
        selected.append(4000)
    global bill     
    bill=0
    for ele in range(0, len(selected)):
        bill = bill + selected[ele]
    output1.set('Total Amount is: %d'% (bill))
        


master = Tk()
Label(master, text="Tailor Billing Program\n Items\t\t\t      Price").grid(row=0, sticky=W) 
var1 = IntVar()
Checkbutton(master, text="Anarkali Suit\t\t3200", variable=var1).grid(row=1, sticky=W)
var2 = IntVar()
Checkbutton(master, text="Suits with pants\t\t1550", variable=var2).grid(row=2, sticky=W)
var3 = IntVar()
Checkbutton(master, text="Salwar suit\t\t1500", variable=var3).grid(row=3, sticky=W)
var4 = IntVar()
Checkbutton(master, text="Designer Kurti\t\t1200", variable=var4).grid(row=4, sticky=W)
var5 = IntVar()
Checkbutton(master, text="Jumpsuit\t\t1800", variable=var5).grid(row=5, sticky=W)
var6 = IntVar()
Checkbutton(master, text="Gowns\t\t\t4000", variable=var6).grid(row=6, sticky=W)
output = StringVar()
outputlabel = Label(master, textvariable = output, justify=LEFT).grid(row = 7)
output1 = StringVar()
outputlabel1 = Label(master, textvariable = output1, justify=LEFT).grid(row = 8)
Button(master, text='Quit', bg='red',command=master.quit).grid(row=9, sticky=S, pady=4)
Button(master, text='Show', bg = 'yellow',command=var_status).grid(row=10, sticky=S, pady=4)
Button(master, text='Pay', bg='green',command=calculate).grid(row=11, sticky=S, pady=4)
mainloop()