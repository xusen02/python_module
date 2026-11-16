import alchemy.grimoire


def main() -> None:
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")

    lt = alchemy.grimoire.light_spell_record('fantasy', 'Earth, wind and fire')

    print(f"Testing record light spell: {lt}")


if __name__ == "__main__":
    main()
