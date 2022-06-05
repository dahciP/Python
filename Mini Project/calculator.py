
def addition(x,y):
    return float(x+y)

def subtraction(x,y):
    return float(x-y)

def multiplication(x,y):
    return float(x*y)

def division(x,y):
    return float(x/y)

print("\nEnter all the elements with a space included between")
a = input("\nEnter operation: ")
s = a.split(" ")
n1 = int(s[0])
sign = s[1]
n2 = int(s[2])
if sign=="+":
    ans = addition(n1,n2)
    print("\nAns. ",ans)
elif sign=='-':
    ans = subtraction(n1,n2)
    print("\nAns. ",ans)
elif sign=='*':
    ans = multiplication(n1,n2)
    print("\nAns. ",ans)
elif sign=='/':
    ans = division(n1,n2)
    print("\nAns. ",ans)

c=1
while c==1:
    b = input("\nEnter operation: ")
    s2 = b.split(" ")
    sign2 = s2[0]
    n3 = int(s2[1])
    if sign2=="+":
        ans = addition(ans,n3)
        print("\nAns. ",ans)
    elif sign2=='-':
        ans = subtraction(ans,n3)
        print("\nAns. ",ans)
    elif sign2=='*':
        ans = multiplication(ans,n3)
        print("\nAns. ",ans)
    elif sign2=='/':
        ans = division(ans,n3)
        print("\nAns. ",ans)
