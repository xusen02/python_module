import random

all_achivement = [
    "Art of Abysswalking",
    "To Link the Fire",
    "Dark Lord",
    "Knight's Honor",
    "The Dark Soul",
    "Warrior of Sunlight",
    "Blade of the Darkmoon",
    "Lordvessel",
    "Rite of Kindling",
    "Way of White",
    "Enkindle",
    "Bond of a Pyromancer",
    "Embrace the Flame",
]


def gen_player_achievements() -> set[str]:
    num = random.randint(3, len(all_achivement))
    return set(random.sample(all_achivement, num))


player0 = gen_player_achievements()
player1 = gen_player_achievements()
player2 = gen_player_achievements()
player3 = gen_player_achievements()

name = [
    "Big Hat Logan",
    "Anastacia of Astora",
    "Crestfallan Merchant",
    "dusk of Oolacile"
]

players = [
    player0,
    player1,
    player2,
    player3
]


print("=== Achievement Tracker System ===\n")

for i in range(len(players)):
    print(f"Player {name[i]}: {players[i]}")

print()
all_distinct = set.union(player0, player1, player2, player3)
print(f"All distinct achievements: {all_distinct}\n")

common = set.intersection(player0, player1, player2, player3)
print(f"Common achievements: {common}\n")

for i in range(len(players)):
    others = set("")

    for j in range(len(players)):
        if i != j:
            others = set.union(others, players[j])

    only_player = set.difference(players[i], others)
    print("Only", name[i], "has:", only_player)

print()
for i in range(len(players)):
    missing_ach = set(all_achivement) - players[i]
    print(f"{name[i]} is missing: {missing_ach}")
