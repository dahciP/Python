with open('C:/Python/PS_4/Files/fourth_1.txt','r') as f1, open('C:/Python/PS_4/Files/fourth_2.txt','w') as f2:
    for line in f1:
        f2.write(line)