import sys
import typing


def recover_file(path: str) -> None:
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{path}'")
    try:
        file: typing.IO[str] = open(path, "r")
    except OSError as e:
        print(f"Error opening file '{path}': {e}")
        return

    try:
        content = file.read()
        print("---")
        print(content, end="")
        if content != "" and not content.endswith("\n"):
            print()
        print("---")
    except (OSError, UnicodeDecodeError) as e:
        print(f"Error reading file '{path}': {e}")

    finally:
        file.close()
        print(f"File '{path}' closed.")


def main() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return
    recover_file(sys.argv[1])


if __name__ == "__main__":
    main()
