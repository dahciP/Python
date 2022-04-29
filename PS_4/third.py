with open("C:/Python/PS_4/Files/third.txt", "rt") as f:
    word = f.read()
    word = word.replace('donkey', 'monkey')

with open("C:/Python/PS_4/Files/third.txt", "wt") as f:
    f.write(word)
