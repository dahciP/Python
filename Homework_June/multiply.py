def sum(numbers,ele):
    total=numbers[0]
    for x in range(1,ele):
        total *= numbers[x]
    return total

numbers=[]
ele = int(input("\nEnter the number of elements: "))
for i in range (0,ele):
    num = int(input())
    numbers.append(num) 

print("\nSum of the numbers is: ",sum(numbers,ele))