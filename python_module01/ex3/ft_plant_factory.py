class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def grow(self):
        self.height += 1

    def show(self):
        print("Created:", self.name + ":", round(self.height, 1),
              "cm,", self.age, "days old")


print("=== Plant Factory Output ===")

rose = Plant("Rose", 25.0, 30)
oak = Plant("Oak", 200.0, 365)
cactus = Plant("Cactus", 5.0, 90)
sunflower = Plant("Sunflower", 80.0, 45)
fern = Plant("Fern", 15.0, 120)

rose.show()
oak.show()
cactus.show()
sunflower.show()
fern.show()
