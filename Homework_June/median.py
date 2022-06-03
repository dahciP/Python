def median(list): #prints middle number
    list.sort()
    print(list)
    print(list[1])

list = []
print("Enter 3 elements : ")
for i in range(0, 3):
    num = int(input())
    list.append(num) 
median(list)  
