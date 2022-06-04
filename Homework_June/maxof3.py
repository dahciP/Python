def max_of_two(x,y):
    if x>y:
        return x
    return y

def max_of_three(x,y,z):
    return max_of_two(x,max_of_two(y,z))

x=int(input("\nEnter first number: "))
y=int(input("\nEnter first number: "))
z=int(input("\nEnter first number: "))
print("\nMaximum of three numbers is: ",max_of_three(x,y,z))