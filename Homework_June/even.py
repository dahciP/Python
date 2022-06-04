def even(list,ele):
    new_list=[]
    for i in range(0,ele):
        if list[i]%2==0:
            new_list.append(list[i])
    return new_list

list=[]
ele=int(input("\nEnter the number of elements in the list: "))
for i in range(0,ele):
    num=int(input())
    list.append(num)

print("\nThe list of even numbers is: ", even(list,ele))