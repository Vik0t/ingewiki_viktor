class Cat():
    name = ""
    color = ''
    weight = 0
    def meow(self):
        print("meow!")

    def __init__(self, newName):
        self.name = newName

    def setColor(self, newColor):
        self.color = newColor

    def getColor(self):
        return self.color

    def setWeight(self, newWeight):
        self.weight = newWeight

    def getWeight(self):
        return self.weight


