showroom = set()

showroom.update(["Cherokee", "Prius", "CyberTruck", "Camaro"])

# print(len(showroom))

showroom.add("Cherokee")

# print(showroom)

showroom.update({"Brougham", "Rodeo"})

# print(showroom)

showroom.discard("Rodeo")

# print(showroom)

junkyard = {"Civic", "Highlander", "ModelS", "Brougham", "Xterra", "Prius"}

print(showroom.intersection(junkyard))

newShowroom = showroom.union(junkyard)

print(newShowroom)