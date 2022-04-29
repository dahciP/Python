#Print star pattern
print("\n\n1. Print star pattern\n")
for i in range (0, 5):
    for j in range(0, i+1):
        print("* ", end='  ')
    print("\n")
for i in range (5, 0, -1):
    for j in range(0, i-1):
        print("* ", end='  ')
    print("\n")

#Find and Print sum
print("\n2. Find and print sum")
m=int(input("\nEnter number of terms: "))
n=int(input("Enter number: "))
temp=n
sum=0

for i in range(0,m):
   print(temp,end=" + ")
   sum += temp
   temp=(temp*10)+n

print("\nThe sum of above equation is: ", sum)

#Calculate the cube of n numbers
print("\n\n3. Calculate the cube of n numbers")
n = int(input("\nEnter the number till you want to find the cube: "))
i=1
while i<=n:
    cube = i*i*i
    print(cube)
    i=i+1

#Print odd index position 
print("\n\n4. Print odd index position")
list = [10,20,40,50,60,70]
print(list)
print("Printing odd index from list")
for i in range(0,7,1):
    if i%2==1:
        print(list[i])

#Print string in reverse
print("\n\n5. Print string in reverse")
string = input("\nEnter your string: ")
print ("The original string is: ",end="")
print (string)
str = ''
for i in string:
    str = i + str
print ("The reversed string is: ",end="")
print (str)

#Find Factorial of a given number
print("\n\n6. Find factorial of a given number")
n = int(input("\nEnter the number for finding factorial: "))
fac = 1
for i in range(1,n+1):
    fac = fac * i
print("Factorial of",n,"is:", fac)

#Print fibanacci series upto n terms
print("\n\n7. Print fibonacci series upto n terms")
fterm=0
sterm=1
n=int(input("\nEnter the number upto which you want to print your fibonacci series"))
print('\nFibonacci series upto n temrs is as follows: ',fterm,sterm,end=" ")
for i in range(2,n):
    sum = fterm + sterm;
    print(sum, end=" ")
    fterm = sterm
    sterm = sum

#Write a program to print all prime numbers within a range
print("\n\n8. Print prime numbers within a given range")
flag = 0    
a=int(input("\nEnter lower bound of the interval:"))
b=int(input("Enter upper bound of the interval:"))
print("\nPrime numbers between", a, "and",b, "are:")
for i in range(a, b + 1):
    if (i == 1):
        continue
    flag = 1    
    for j in range(2, int(i / 2 + 1)):
        if (i % j == 0):
            flag = 0
            break
    if (flag == 1):
        print(i, end = " ")

#Display numbers from -100 to -1 using for loop
print("\n\n9. Display numbers from -100 to -1")
for i in range(-100, 0):
    if i%10==0:
        print('\n')
    print(i, end=' ')
    i=i-1
                
#Print list in reverse order
print('\n\n10. Print list in reverse order\n')
list = [10,20,40,50,60,70]
list.reverse()
print(list)

#Print number pattern
print("\n\n11. Print number pattern\n")

for i in range (5, 0, -1):
    for j in range(i,0,-1):
        print(j, end='  ')
    print("\n")

#Count total number of digits in the number
print('\n\n12. Count number of digits')
n = int(input("\nEnter the number: "))
count = 0
while n != 0:
    n = int(n/ 10)
    count += 1
print("Number of digits: ", count)

#Print from the list that satisfy the condition
print('\n\n13. Print those numbers which satisfy the condition')
plist=[]
index=0
n=int(input('\nEnter the number of elements in the list: '))
print('\n')
while index<n:
    ins = int(input('Enter the number you want to append in the list: '))
    plist.insert(index, ins)
    index+=1
print("\nThe original list is as follows: ", plist)
olist=[]
oindex=0
for i in range(0,n):
    if plist[i]%5==0:
        if plist[i]>500:
            break
        if plist[i]>150:
            continue
        else:
            olist.insert(oindex, plist[i])
            oindex+=1
print('\nList after going through all conditions: ',olist)

#Calculate sum of all numbers from 1 to given number
print('\n\n14. Calculate sum till given number')
n=int(input("\nEnter the number till which you want to find the sum: "))
sum=0
for i in range(1,n+1):
    sum = sum+i
print(sum)
