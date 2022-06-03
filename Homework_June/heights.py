def height(list): #prints top 3 heights in descending order
    list.sort()
    list.reverse()
    print("\nThe top 3 buildings are: \n")
    for i in range(0,3):
        print(list[i])

heights = []
print("Enter heights for 8 buildings : ")
for i in range(0, 8):
    num = int(input())
    heights.append(num) 
height(heights) 