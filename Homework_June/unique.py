def unique_list(l):
    x=[]
    for a in l:
        if a not in x:
            x.append(a)
    return x

list=[]
ele = int(input("\nEnter the number of elements: "))
for i in range(0,ele):
    num = int(input())
    list.append(num)
print(unique_list(list))