import math


def to_float(text: str) -> float:
    try:
        return float(text)
    except ValueError as e:
        raise ValueError(f"Error on parameter '{text}': {e}")


def get_player_pos() -> tuple[float, float, float]:
    while True:
        text = input("Enter new coordinates as floats in format 'x,y,z': ")
        try:
            x, y, z = text.split(",")
        except ValueError:
            print("Invalid syntax")
            continue
        try:
            return (to_float(x), to_float(y), to_float(z))
        except ValueError as e:
            print(e)


def distance(a: tuple[float, float, float],
             b: tuple[float, float, float]) -> float:
    x1, y1, z1 = a
    x2, y2, z2 = b
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def main() -> None:
    print("=== Game Coordinate System ===")

    print("\nGet a first set of coordinates")
    first = get_player_pos()
    print(f"Got a first tuple: {first}")
    x, y, z = first
    print(f"It includes: X={x}, Y={y}, Z={z}")
    print(f"Distance to center: {round(distance((0, 0, 0), first), 4)}")

    print("\nGet a second set of coordinates")
    second = get_player_pos()
    print("Distance between the 2 sets of coordinates: "
          f"{round(distance(first, second), 4)}")


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nInput interrupted, exiting.")
