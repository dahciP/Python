d1 = {"Brand" : "McLaren", 
      "Model" : "720s", 
      "Version" : "Coupe", 
      "Colour" : "Onyx Black"}

d2 = {"Engine " : "V8 4 valves",
      "Transmission" : "7-speed AT",
      "Fuel" : "Petrol", 
      "Drivetrain" : "RWD"}

d1.update(d2)
print(d1)

print(list(d2.keys()))
print(d1.values())
print(d2.items())
print(d1["Version"])
