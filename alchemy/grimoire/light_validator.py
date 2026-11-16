def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients
    condition = light_spell_allowed_ingredients()
    in_hand = ingredients.lower().replace(",", " ").split()
    for item in in_hand:
        if item.strip() in condition:
            return f"({list(set(in_hand).intersection(condition))} -VALID)"
    return f"({ingredients} -INVALID)"
