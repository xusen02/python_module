class Plant:
    def __init__(self, name, height, age):
        self.name = name.capitalize()
        self.height = float(height)
        self.days_old = age

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.days_old} days old")


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        self.bloomed = False

    def bloom(self):
        self.bloomed = True

    def show(self):
        super().show()
        print(f" Color: {self.color}")
        if (self.bloomed):
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} is not bloomed yet")


class Tree(Plant):
    def __init__(self, name, height, age,  trunk_diameter):
        super().__init__(name, height, age)
        self. trunk_diameter = float(trunk_diameter)
        self.shade = 0

    def produce_shade(self):
        self.shade += 1
        print(
            f" Tree {self.name} now produces a shade "
            f"of {self.height}cm long and "
            f"{self.trunk_diameter}cm wide."
        )

    def show(self):
        super().show()
        print(f" Trunk diameter: {self. trunk_diameter}")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0
        self.days_old = age

    def age(self):
        self.days_old += 20

    def grow(self):
        self.height += 42
        self.nutritional_value += 20

    def show(self):
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")


rose = Flower("Rose", 15, 12, "red")
oak = Tree("Oak", 200, 365, 5)
tomato = Vegetable("Tomato", 5, 10, "April")

print("=== Garden Plant Types ===")
print("=== Flower")
rose.show()
print("[asking the rose to bloom]")
rose.bloom()
rose.show()
print()
print("=== Tree")
oak.show()
print("[asking the oak to produce shade]")
oak.produce_shade()
print()
print("=== Vegetable")
tomato.show()
print("[make tomato grow and age for 20 days]")
tomato.age()
tomato.grow()
tomato.show()
