a = input("Enter a String: ")
if a.find("  ") == -1:
    print("Contains no double space")
else:
    print("Contains double space")
    print("Replacing the double space with single space: ")
    print(a.replace("  " , " " ))