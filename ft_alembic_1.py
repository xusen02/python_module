import alchemy

print("=== Alembic 1 ===")
print("Accessing the alchemy module using 'import alchemy'")
print(f"Testing create_air: {alchemy.create_air()}")
print(
    "Now show that not all functions can be reached\n"
    "This will raise an exception!\n"
    )
print("Testing the hidden create_earth: ")
print(f"[{alchemy.create_earth()}]")
