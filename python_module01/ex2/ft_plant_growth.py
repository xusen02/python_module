class Plant:
    def __init__(self, name, init_height, age=0):
        self.name = name
        self.height = init_height
        self.age_days = age

    def grow(self):
        self.height += 0.5

    def age(self):
        self.age_days += 1

    def show_status(self):
        print("=== Garden Plant Growth ===")
        init_height = self.height

        print(f"{self.name} : {self.height}cm, {self.age_days} days old")
        for day in range(1, 8):
            print(f"=== Day {day} ===")
            self.grow()
            self.age()
            print(f"{self.name}: {self.height}cm, {self.age_days} days old")

        total_increases = self.height - init_height
        print(f"Growth this week: {total_increases}cm")


my_plant = Plant(name="carrot", init_height=0.0, age=42)

garden_plants = [my_plant]

my_plant.show_status()
