def garden_operations(operation_number):
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        10 / 0
    elif operation_number == 2:
        open("missing_garden_file.txt", "r")
    elif operation_number == 3:
        "Flowers" + 42
    else:
        return


def test_error_types():
    print("=== Garden Error Types Demo ===")
    try:
        print("Testing operation 0...")
        garden_operations(0)
    except ValueError as error:
        print(f"Caught ValueError: {error}")

    try:
        print("Testing operation 1...")
        garden_operations(1)
    except ZeroDivisionError as error:
        print(f"Caught ZeroDivisionError: {error}")

    try:
        print("Testing operation 2...")
        garden_operations(2)
    except FileNotFoundError as error:
        print(f"Caught FileNotFoundError: {error}")

    try:
        print("Testing operation 3...")
        garden_operations(3)
    except TypeError as error:
        print(f"Caught TypeError: {error}")

    try:
        print("Testing operation 4...")
        garden_operations(4)
    except Exception as error:
        print(f"Caught TypeError: {error}")

    print("Operation completed successfully\n")
    print("All error types tested successfully!")


test_error_types()
