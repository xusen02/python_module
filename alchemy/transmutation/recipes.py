from elements import create_fire
from ..potions import strength_potion
from ..elements import create_air


def lead_to_gold():
    return ("Recipe transmuting Lead to"
            f"Gold: brew '{create_air()}' and '{strength_potion()}'"
            f"mixed with '{create_fire()}'")
