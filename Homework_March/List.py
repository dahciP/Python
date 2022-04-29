prime7= [7, 17, 37, 47, 67]
vgames = ["Minecraft", "GTA5", "Halo", "CSGO", "Fortnite"]
random = [23, 42, 12, 56, 57, 23]

leap = (2000, 2004, 2008, 2012, 2016, 2020)
country = ("China", "India", "USA", "Indonesia", "Pakistan", "Brazil")

print("\nList of prime numbers ending with 7: ", prime7)
print("\nList of video games: ",vgames)
print("\nList of random numbers: ",random)
print("\nTuple of leap years since 2000: ", leap)
print("\nTuple of countries according to population: ", country)

insert = int(input("\nEnter a prime number ending with 7: "))
prime7.append(insert)
print("\nList of prime numbers ending with 7 is: ", prime7)
print("\nPosition of Halo in the list: ",vgames.index("Halo"))
random.sort()
print("\nSorted list is ", random)
vgames.pop()
print("\nAfter poping",vgames)
print("\nNumber of times 23 occured: ",random.count(23))
prime7.clear()
print("\nCleared list of prime: ", prime7)

print("\nNumber of times 2004 appeared in tuple ",leap.count(2004))
print("\nPosition of India in the tuple: ", country.index("India"))