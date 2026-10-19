def ft_print(plant: str, height: int, age: int) -> None:
    print("=== Welcome to My Garden ===")
    print(f"Plant: {plant}")
    print(f"Height: {height}cm")
    print(f"Age: {age} days\n")
    print("=== End of Program ===")


def main() -> None:
    plant = "Rose"
    height = 25
    age = 30
    ft_print(plant, height, age)


if __name__ == "__main__":
    main()
