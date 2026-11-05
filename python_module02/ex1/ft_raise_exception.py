def input_temperature(temp_str):
    temperature = int(temp_str)

    if temperature < 0:
        raise ValueError(f"{temperature}°C is too cold for plants (min 0°C)")
    elif temperature > 40:
        raise ValueError(f"{temperature}°C is too hot for plants (max 40°C)")
    else:
        return temperature


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

    print("Input data is '100'")
    try:
        print(f"Temperature is now {input_temperature('100')}°C\n")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}\n")

    print("Input data is '-50'")
    try:
        print(f"Temperature is now {input_temperature('-50')}°C\n")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}\n")

    print("All tests completed - program didn't crash!")


test_temperature()
