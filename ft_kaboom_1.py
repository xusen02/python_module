def main() -> None:
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")

    import alchemy.grimoire
    alchemy.grimoire.dark_spell_record('awatakatawa', 'frog, 42 and pp')


if __name__ == "__main__":
    main()
