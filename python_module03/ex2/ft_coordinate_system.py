import math


def check_syntax(get_lct: str) -> int:
    if "," not in get_lct:
        print("Invalid syntax")
        return 0
    return 1


def turn_to_tuple(get_lct: str) -> tuple[float, float, float] | None:
    store = get_lct.split(",")

    if len(store) != 3:
        print(
            "Invalid input (input must be 3 numbers and "
            "separated by using ',')"
        )
        return None

    result: list[float] = []
    for num in store:
        try:
            result.append(float(num))
        except ValueError as error:
            print(f"Error on parameter '{num}': {error}")
            return None

    return (result[0], result[1], result[2])


def calu_distant(
    coordinates1: tuple[float, float, float],
    coordinates2: tuple[float, float, float],
) -> float:
    x = (coordinates1[0] - coordinates2[0]) ** 2
    y = (coordinates1[1] - coordinates2[1]) ** 2
    z = (coordinates1[2] - coordinates2[2]) ** 2

    result = math.sqrt(x + y + z)
    return result


def get_player_pos() -> None:
    print("Get a first set of coordinates")
    coordinates: tuple[float, float, float] | None = None

    while coordinates is None:
        get_lct = input(
            "Enter new coordinates as floats in format 'x,y,z': "
        )
        if check_syntax(get_lct) == 0:
            return
        coordinates = turn_to_tuple(get_lct)

    assert coordinates is not None

    print(f"Got a first tuple: {coordinates}")
    print(
        f"It includes: X={coordinates[0]}, "
        f"Y={coordinates[1]}, "
        f"Z={coordinates[2]}"
    )

    st_to_center = calu_distant(coordinates, (0.0, 0.0, 0.0))
    print(f"Distance to center: {round(st_to_center, 4)}")

    print("\nGet a second set of coordinates")
    coordinates1: tuple[float, float, float] | None = None

    while coordinates1 is None:
        get_lct = input(
            "Enter new coordinates as floats in format 'x,y,z': "
        )
        if check_syntax(get_lct) == 0:
            continue
        coordinates1 = turn_to_tuple(get_lct)

    assert coordinates1 is not None

    dist_between_players = calu_distant(coordinates, coordinates1)
    print(
        f"Distance between the 2 sets of coordinates: "
        f"{dist_between_players:.4f}"
    )


print("=== Game Coordinate System ===\n")

get_player_pos()
