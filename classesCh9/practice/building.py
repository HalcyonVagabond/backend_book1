import datetime

class Building:
    def __init__(self, address, stories):
        self.address = address
        self.stories = stories
        self.owner = ""
        self.designer = ""
        self.date_constructed = ""

    def construct(self):
        self.date_constructed = datetime.datetime.now()

    def purchase(self, owner):
        self.owner = owner

    def printBuildingInfo(self):
        print(f"{self.address} was purchased by {self.owner} on {self.date_constructed} and has {self.stories} stories.")


oleMcDonaldsHeadquarters = Building("123 McNugget St.", 70)
oleMcDonaldsHeadquarters.construct()
oleMcDonaldsHeadquarters.purchase("McBuilder")
oleMcDonaldsHeadquarters.printBuildingInfo()

batmanBuilding = Building("555 Batcave Blvd.", -50)
batmanBuilding.purchase("Bruce Wayne")
batmanBuilding.construct()
batmanBuilding.printBuildingInfo()



