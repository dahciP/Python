def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)

n = int(input("\nInput a number for fact: "))
print("\nFactorial is: ",fact(n))