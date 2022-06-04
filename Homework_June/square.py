def square():
    list=[]
    for i in range(1,31):
        multiply = i*i
        list.append(multiply)
    return list

print("\nThe list of square of numbers is: \n", square())