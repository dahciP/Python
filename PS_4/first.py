word = 'twinkle'
with open("C:/Python/PS_4//Files/First.txt", "r") as f:
    filereader = f.read()
    if word in filereader: 
        print('Word', word, 'is in the file First.txt')
    else: 
        print('String', word , 'is not in the file First.txt') 
