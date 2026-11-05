def input_temperature(temp_str):
    return int(temp_str)


def test_temperature():
    print("=== Garden Temperature ===\n")
    print("Input data is '25'")
    try:
        print(f"Temperature is now {input_temperature('25')}°C\n")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}\n")

    print("Input data is 'abc'")
    try:
        print(f"Temperature is now {input_temperature('abc')}°C\n")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}\n")

    print("All teste completed - program didn't crash!")


test_temperature()
