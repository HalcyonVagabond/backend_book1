zoo = ("giraffe","zebra","tiger","bear","anteater","penguin","groundhog","lemur","kangaroo","pengolin")

print(zoo.index("penguin"))

def animalSearch(animal):
    if animal in zoo:
        print(f"We have {animal}s here!")
    else:
        print(f"Sorry, we don't have {animal}s :/")

animalSearch("zebra")
animalSearch("opossum")

(animal1, animal2, animal3, animal4, animal5, animal6, animal7, animal8, animal9, animal10) = zoo

print(animal1)
print(animal4)

zooList = list(zoo)

zooList.extend(["prairiedog", "orangutan", "otter"])

zoo = tuple(zooList)

print(zoo)