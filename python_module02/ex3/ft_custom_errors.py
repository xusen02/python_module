class GardenError(Exception):
    def __init__(self, message="Unknow garden error"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message="Unknown plant error"):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message="Unknown water error"):
        super().__init__(message)


def check_plant(plant):
    if plant not in ("rose", "sunflower", "tomato"):
        raise PlantError(f"The {plant} plant is wilting!")


def check_tank(water):
    if float(water) <= 0:
        raise WaterError("Not enough water in the tank!")


print("=== Custom Garden Errors Demo ===\n")
try:
    print("Testing PlantError...")
    check_plant("cat")
except PlantError as error:
    print(f"Caught PlantError: {error}\n")

try:
    print("Testing WaterError...")
    check_tank(0)
except WaterError as error:
    print(f"Caught WaterError: {error}\n")

print("Testing catching all garden errors...")
try:
    check_plant("cat")
except GardenError as error:
    print(f"Caught PlantError: {error}")

try:
    check_tank(0)
except GardenError as error:
    print(f"Caught WaterError: {error}\n")

print("All custom error types work correctly!")

print("=== Testing Default Error Messages ===")

try:
    raise GardenError()
except GardenError as error:
    print(f"GardenError: {error}")

try:
    raise PlantError()
except PlantError as error:
    print(f"PlantError: {error}")

try:
    raise WaterError()
except WaterError as error:
    print(f"WaterError: {error}")
