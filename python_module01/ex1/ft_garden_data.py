class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


plant_one = Plant(name="Tomato", height=45, age=60)
plant_two = Plant(name="Rose", height=20, age=6)
plant_three = Plant(name="Sunflower", height=120, age=42)

garden_plants = [plant_one, plant_two, plant_three]

print("=== Garden Plant Registry ===")

for plant in garden_plants:
    plant.show()
