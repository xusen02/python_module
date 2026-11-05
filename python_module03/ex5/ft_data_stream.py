import random
from typing import Generator


def gen_event() -> Generator[tuple[str, str], None, None]:
    players = [
        "Yhorm the Giant",
        "Black Hand Kamui",
        "Orbeck of Vinheim",
        "Yuria of Londor"
    ]
    actions = [
        "run",
        "light attack",
        "strong attack",
        "casting spells",
        "gose hollow"
    ]

    while True:
        name = random.choice(players)
        action = random.choice(actions)
        yield (name, action)


event_generator = gen_event()

for i in range(1000):
    name, action = next(event_generator)
    print(f"Event {i}: Player {name} did action {action}")

events = [next(gen_event()) for _ in range(10)]
print("Built list of 10 events:", events)


def consume_event(
    events: list[tuple[str, str]],
) -> Generator[tuple[str, str], None, None]:
    while len(events) > 0:
        index = random.randrange(len(events))
        yield events.pop(index)


for event in consume_event(events):
    print("Got event from list:", event)
    print("Remains in list:", events)
