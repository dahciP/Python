

c=1
while c==1:
    value = int(input("\nEnter your income : "))
    if value<=500000:
        tax = 0
        print("Tax on your income is 0 percent which will be: ",tax," rupees")
    elif value>500000 & value<=2000000:
        tax = 0.03*value
        print("Tax on your income is 3 percent which will be: ",tax," rupees")
    elif value>2000000 & value<=5000000:
        tax = 0.05*value
        print("Tax on your income is 5 percent which will be: ",tax," rupees")
    elif value>5000000 & value<=10000000:
        tax = 0.08*value
        print("Tax on your income is 8 percent which will be: ",tax," rupees")
    elif value>10000000:
        tax = 0.12*value
        print("Tax on your income is 12 percent which will be: ",tax," rupees")
    else:
        print("\nError!! :(") 
    c = int(input("\nPress 1 if you want to re-calculate, else press 0: ")) 

