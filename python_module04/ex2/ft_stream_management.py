import sys

if len(sys.argv) < 2:
    print("Error: No filename provided.", file=sys.stderr)
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
    print(f"Error opening file '{filename}': {error}", file=sys.stderr)
    sys.exit(1)

print("Transform data:")

try:
    file = open(filename, "r")
    print("second try blok")
    content = file.read()
    file.close()

    lines = content.splitlines()
    modifield = ""

    for line in lines:
        modifield += line + "#\n"
    print("---\n")
    print(modifield)
    print("---\n")

    print("\nEnter new file name (or empty): ", end="")
    savefile = sys.stdin.readline().rstrip("\n")

    if savefile:
        output_file = open(savefile, "w")
        output_file.write(modifield)
        output_file.close()
        print(f"Saving data to '{savefile}'")
        print(f"Data saved in file '{savefile}'.")
    else:
        print("Not saving data.")
except Exception as error:
    print(f"Archive error: {error}", file=sys.stderr)
    sys.exit(1)
sys.exit()
