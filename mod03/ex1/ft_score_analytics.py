import sys


def main() -> None:
    print("=== Player Score Analytics ===")
    scores: list[int] = []
    for arg in sys.argv[1:]:
        try:
            scores.append(int(arg))
        except ValueError:
            print(f"Invalid parameter: '{arg}'")

    if len(scores) == 0:
        print("No scores provided. Usage: "
              f"python3 {sys.argv[0]} <score1> <score2> ...")
        return

    total = sum(scores)
    high = max(scores)
    low = min(scores)
    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {total}")
    print(f"Average score: {total / len(scores)}")
    print(f"High score: {high}")
    print(f"Low score: {low}")
    print(f"Score range: {high - low}")


if __name__ == "__main__":
    main()
