
class Plant:

    def __init__(self, name, height, age):
        self.name = name.capitalize()
        self.height = float(height)
        self.days_old = age
        self.statistics = Plant.Statistics()

    # Nested class for statistical data
    class Statistics:
        def __init__(self):
            self.__grow_count = 0
            self.__age_count = 0
            self.__show_count = 0
            self.__shade_count = 0

        def record_grow(self):
            self.__grow_count += 1

        def record_age(self):
            self.__age_count += 1

        def record_show(self):
            self.__show_count += 1

        def record_shade(self):
            self.__shade_count += 1

        def display(self, plant):
            print(f"[statistics for {plant.name}]")
            print(
                f"State: {self.__grow_count} grow, "
                f"{self.__age_count} age, "
                f"{self.__show_count} show"
            )

            if isinstance(plant, Tree):
                print(f" {self.__shade_count} shade")

    def grow(self):
        self.height += 1
        self.statistics.record_grow()

    def age(self):
        self.days_old += 1
        self.statistics.record_age()

    def show(self):
        print(
            f"{self.name}: {self.height}cm, "
            f"{self.days_old} days old"
        )
        self.statistics.record_show()

    @staticmethod
    def is_older_than_year(age):
        return age > 365

    @classmethod
    def anonymous(cls):
        return cls("Anonymous", 0, 0)


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        self.bloomed = False

    def grow(self):
        super().grow()
        self.height += 8

    def bloom(self):
        self.bloomed = True
        self.grow()

    def show(self):
        super().show()
        print(f" Color: {self.color}")

        if self.bloomed:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet.")


class Seed(Flower):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age, color)
        self.seed = 0

    def bloom(self):
        super().bloom()
        self.age()
        self.seed += 42

    def show(self):
        super().show()
        print(f" Seeds: {self.seed}")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = float(trunk_diameter)
        self.shade = 0

    def produce_shade(self):
        self.shade += 1
        self.statistics.record_shade()

        print(
            f" Tree {self.name} now produces a shade "
            f"of {self.height}cm long and "
            f"{self.trunk_diameter}cm wide."
        )

    def show(self):
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}")


# Standalone function (not part of any class)
def display_statistics(plant):
    plant.statistics.display(plant)


# Create plants
rose = Flower("Rose", 15, 12, "red")
sunflower = Seed("Sunflower", 80, 45, "yellow")
oak = Tree("Oak", 200, 365, 5)
anonymous_plant = Plant.anonymous()


print("=== Garden statistics ===")

print("=== Check year-old ===")
print(
    f"Is 30 days more than a year? -> "
    f"{Plant.is_older_than_year(30)}"
)
print(
    f"Is 400 days more than a year? -> "
    f"{Plant.is_older_than_year(400)}"
)

print()
print("=== Flower ===")
rose.show()
display_statistics(rose)

print("[asking the rose to bloom]")
rose.bloom()
rose.show()
display_statistics(rose)

print()
print("=== Tree ===")
oak.show()
display_statistics(oak)

print("[asking the oak to produce shade]")
oak.produce_shade()
display_statistics(oak)

print()
print("=== Seed ===")
sunflower.show()
display_statistics(sunflower)

print("[asking the sunflower to bloom]")
sunflower.bloom()
sunflower.show()
display_statistics(sunflower)

print()
print("=== Anonymous ===")
anonymous_plant.show()
display_statistics(anonymous_plant)
