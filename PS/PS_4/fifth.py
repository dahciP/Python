with open("C:/Python/PS_4/Files/fifth_1.txt", "r") as f1, open("C:/Python/PS_4/Files/fifth_2.txt", "r") as f2:    
    i = 0
    for line1 in f1:
        i += 1
        for line2 in f2:
            if line1 == line2:  
                print("Line", i, "is identical")       
            else:
                print("Line", i, "is not identical")
            break
