from re import S


def up_low(s):      
    u = sum(1 for i in s if i.isupper())
    l = sum(1 for i in s if i.islower())
    print( "\nNo. of Upper case characters : %s\nNo. of Lower case characters : %s" % (u,l))

s=input("\nEnter a string: ")
up_low(s)