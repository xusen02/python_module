from .dark_validator import dark_validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    validation = dark_validate_ingredients(ingredients)
    if "INVALID" in validation:
        return f"An Iq too high: {spell_name} -{validation}"
    return f"succes: {spell_name} -{validation}"
