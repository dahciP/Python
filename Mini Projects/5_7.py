def find():
    list=[]
    for i in range (1500,2701):
        if i%7==0:
            if i%5==0:
                list.append(i)
    print(list)

find()