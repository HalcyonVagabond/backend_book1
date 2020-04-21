class Pizza:
    def __init__(self, size, crust = "regular", toppings = ["cheese"] , sauce = "tomato"):
        self.size = size
        self.crust = crust
        self.toppings = toppings
        self.sauce = sauce
    
    def addTopping(self, topping):
        self.toppings.append(topping)

    def printPizza(self):
        print(f"I would like a {self.size} pizza, {self.crust} with {self.sauce} sauce, with {(' ,'.join(self.toppings))} for toppings.")


myPizza1 = Pizza("large")
myPizza1.printPizza()
myPizza1.size = "small"
myPizza1.toppings.extend(["banana peppers", "jalapenos"])
myPizza1.addTopping("potatoes")
print(myPizza1.toppings)
myPizza1.printPizza()

myPizza2 = Pizza("extra-large", "thin-crust", ["cheese", "spinach"], "white")
myPizza2.addTopping("mushrooms")
myPizza2.printPizza()