import random


player = [
    "Big Hat Logan",
    "anastacia of Astora",
    "crestfallan Merchant",
    "dusk of Oolacile",
    "yhorm the Giant",
    "Black Hand Kamui",
    "orbeck of Vinheim",
    "Yuria of Londor"
]

print("=== Game Data Alchemist ===\n")
print(f"Initial list of players: {player}")
capitalized_list = [name.capitalize() for name in player]
print(f"New list with all names capitalized: {capitalized_list}")
capitalized_only = [name for name in player if name[0].isupper()]
print(f"New list of capitalized names only: {capitalized_only}")
print()
player_data = {
    name: random.randint(0, 1000)
    for name in capitalized_list
}
print(f"Score dict: {player_data}")
average = round(sum(player_data.values()) / len(player_data), 2)
print(f"Score average is {average}")

high_scores = {
    name: score
    for name, score in player_data.items()
    if score > average
}
print(f"High scores: {high_scores}")
