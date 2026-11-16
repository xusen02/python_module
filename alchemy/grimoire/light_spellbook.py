from .light_validator import validate_ingredients


def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    validation = validate_ingredients(ingredients)
    if "INVALID" in validation:
        return f"An Iq too high: {spell_name} -{validation}"
    return f"succes: {spell_name} -{validation}"
