import random

ACHIEVEMENTS = [
    "First Steps", "Boss Slayer", "Speed Runner", "Treasure Hunter",
    "Master Explorer", "Crafting Genius", "World Savior", "Survivor",
    "Collector Supreme", "Untouchable", "Strategist", "Unstoppable",
    "Sharp Mind", "Hidden Path Finder", "Dragon Tamer", "Night Owl",
    "Lucky Strike", "Perfectionist", "Team Player", "Lone Wolf",
]


def gen_player_achievements() -> set[str]:
    count = random.randint(8, 12)
    return set(random.sample(ACHIEVEMENTS, count))


def main() -> None:
    print("=== Achievement Tracker System ===\n")
    players = [
        ("Alice", gen_player_achievements()),
        ("Bob", gen_player_achievements()),
        ("Charlie", gen_player_achievements()),
        ("Dylan", gen_player_achievements()),
    ]
    for name, achievements in players:
        print(f"Player {name}: {achievements}")

    distinct: set[str] = set()
    common = players[0][1]
    for _, achievements in players:
        distinct = distinct.union(achievements)
        common = common.intersection(achievements)
    print(f"\nAll distinct achievements: {distinct}")
    print(f"\nCommon achievements: {common}\n")

    for name, achievements in players:
        only = achievements
        for other_name, other in players:
            if other_name != name:
                only = only.difference(other)
        print(f"Only {name} has: {only}")
    print()

    for name, achievements in players:
        missing = set(ACHIEVEMENTS).difference(achievements)
        print(f"{name} is missing: {missing}")


if __name__ == "__main__":
    main()
