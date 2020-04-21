my_family = {
    "sister": {
        "name": "Krista",
        "age": 42
    },
    "mother": {
        "name": "Cathie",
        "age": 70
    },
    "brother": {
        "name": "Paul",
        "age": 38
    },
    "grandmother": {
        "name": "Viola",
        "age": 90
    }
}

myFamilyMembers = [f"{list(value.items())[0][1]} is my {key} and is {str(list(value.items())[1][1])} years old." for (key, value) in list(my_family.items())]

for members in myFamilyMembers:
    print(members)