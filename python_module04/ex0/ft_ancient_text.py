import sys

if len(sys.argv) < 2:
    print("Error: No filename provided.")
    sys.exit()

print("=== Cyber Archives Recovery ===")

filename = sys.argv[1]

try:
    print(f"Accessing file '{filename}'")

    file = open(filename, "r")
    print("---\n")
    print(file.read())
    print("\n---")
    file.close()
    print(f"File '{filename}' closed.")

except Exception as error:
    print(f"Error opening file '{filename}': {error}")

sys.exit()
