import sys

if len(sys.argv) < 2:
    print("Error: No filename provided.")
    sys.exit(1)

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
    sys.exit(1)

print("Transform data:")

try:
    file = open(filename, "r")
    content = file.read()
    file.close()

    lines = content.splitlines()
    modifield = ""

    for line in lines:
        modifield += line + "#\n"
    print("---\n")
    print(modifield)
    print("---")
    savefile = input("Enter new file name (or empty): ")

    if savefile:
        output_file = open(savefile, "w")
        output_file.write(modifield)
        output_file.close()
        print(f"Saving data to '{savefile}'")
        print(f"Data saved in file '{savefile}'.")
    else:
        print("Not saving data.")
except Exception as error:
    print(f"Archive error: {error}")
    sys.exit(1)
sys.exit()
