print("\t\t*****Simple Calculator Program*****")
print("\n\n1. Addition\n2. Subtraction\n3. Multiplicationn\n4. Division")

c=1
while c==1:
    x = int(input("\nEnter your choice for the calculation you want to perform: "))
    if x==1:
        a1 = int(input("\nEnter the first number you want to add: "))
        a2 = int(input("\nEnter the second number you want to add: "))
        add = a1 + a2
        print("\nAns. ",add)
    elif x==2:
        s1 = int(input("\nEnter the first number you want to subtract: "))
        s2 = int(input("\nEnter the second number you want to subtract: "))
        if s1>s2:
            sub = s1-s2
        else:
            sub = s2-s1
        print("\nAns. ",sub)
    elif x==3:
        m1 = int(input("\nEnter the first number you want to multiply: "))
        m2 = int(input("\nEnter the second number you want to multiply: "))
        mul = m1*m2
        print("\nAns. ",mul)
    elif x==4:
        d1 = int(input("\nEnter the first number you want to divide: "))
        d2 = int(input("\nEnter the second number you want to divide: "))
        div = d1/d2
        print("\nAns. ",round(float(div),2))
    else:
        print("\nWrong Input!!")
    c = int(input("\nEnter 1 to do another calculation: "))

#Code by Chinmay Pichad
