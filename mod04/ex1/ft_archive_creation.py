import sys
import typing


def display(content: str) -> None:
    print("---")
    print(content, end="")
    if content != "" and not content.endswith("\n"):
        print()
    print("---")


def read_file(path: str) -> str | None:
    print(f"Accessing file '{path}'")
    try:
        file: typing.IO[str] = open(path, "r")
    except OSError as e:
        print(f"Error opening file '{path}': {e}")
        return None
    content: str | None = None
    try:
        content = file.read()
        display(content)
    except (OSError, UnicodeDecodeError) as e:
        print(f"Error reading file '{path}': {e}")
    finally:
        file.close()
        print(f"File '{path}' closed.")
    return content


def transform(content: str) -> str:
    result = ""
    for line in content.splitlines():
        result += line + "#\n"
    return result


def write_file(path: str, content: str) -> None:
    print(f"Saving data to '{path}'")
    try:
        file: typing.IO[str] = open(path, "w")
    except OSError as e:
        print(f"Error opening file '{path}': {e}")
        return
    try:
        file.write(content)
        print(f"Data saved in file '{path}'.")
    except OSError as e:
        print(f"Error writing file '{path}': {e}")
    finally:
        file.close()


def main() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return
    print("=== Cyber Archives Recovery & Preservation ===")
    content = read_file(sys.argv[1])
    if content is None:
        return
    new_content = transform(content)
    print("Transform data:")
    display(new_content)
    try:
        name = input("Enter new file name (or empty): ")
    except (EOFError, KeyboardInterrupt):
        print("\nInput interrupted, not saving data.")
        return
    if name == "":
        print("Not saving data.")
        return
    write_file(name, new_content)


if __name__ == "__main__":
    main()
