import sys

inventory: dict[str, int] = {}
total_item: int = 0
total_quantity: int = 0

print("=== Inventory System Analysis ===")


for arg in sys.argv[1:]:
    parts: list[str] = arg.split(":")

    if len(parts) != 2 or not parts[0] or not parts[1]:
        print(f"Error: Invalid parameter '{arg}'")
        continue

    name: str = parts[0]

    if name in inventory:
        print(f"Redundant item '{name}' - discarding")
        continue

    try:
        quantity = int(parts[1])
    except ValueError as error:
        print(f"Quantity error for '{name}': {error}")
        continue

    if quantity < 0:
        print(f"Error: Negative quantity for '{name}'")
        continue

    total_item += 1
    total_quantity += quantity
    if name and quantity:
        inventory.update({name: quantity})
    else:
        continue

print(f"Got inventory: {list(inventory.keys())}")
if inventory and total_quantity:
    print(f"Total quantity of the {total_item} item: {total_quantity}")
else:
    sys.exit()


compare: list[int] = list(inventory.values())
items: list[str] = list(inventory.keys())

for num in range(len(compare)):
    print(
        f"Item {items[num]} represents "
        f"{round((compare[num]/total_quantity) * 100, 1)}%"
    )

least_num: int = compare[0]
highest_num: int = compare[0]
key_least_item: int = 0
key_highest_item: int = 0

for num in range(len(compare)):
    if least_num > compare[num]:
        least_num = compare[num]
        key_least_item = num

    if highest_num < compare[num]:
        highest_num = compare[num]
        key_highest_item = num

least_item: str = items[key_least_item]
highest_item: str = items[key_highest_item]

print(f"Item most abundant: {highest_item} with quantity {highest_num}")
print(f"Item least abundant: {least_item} with quantity {least_num}")
print(f"Updated inventory: {inventory}")
