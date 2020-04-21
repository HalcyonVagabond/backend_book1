planet_list = ["Mercury", "Mars"]

planet_list.append("Jupiter")
planet_list.append("Saturn")

# print(planet_list)

planet_list.extend(["Uranus", "Neptune"])

# print(planet_list)

planet_list.insert(1, "Venus")
planet_list.insert(2, "Earth")

# print(planet_list)

planet_list.append("Pluto")

# print(planet_list)

rocky_planets = planet_list[0:4]

# print(f"Rocky planets:{rocky_planets}")

# planet_list.__delitem__(8)
del(planet_list[8])

# print(planet_list)

# **** Begin Challenge: Iterating over planets *******

spacecrafts = [
   ("Cassini", "Saturn"),
   ("Viking", "Mars"),
   ("Galileo", "Jupiter"),
   ("Vega", "Venus"),
]

for planet in planet_list:
    for craft in spacecrafts:
        if craft[1] == planet:
            print(f"{planet} was visited by {craft[0]}!")