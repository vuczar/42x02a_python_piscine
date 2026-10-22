class Plant():
    def __init__(
            self,
            name: str,
            s_height: float,
            s_age: int,
            growth: float = 0.8
            ) -> None:
        self.name = name
        self.s_height = s_height
        self.height = s_height
        self.s_age = s_age
        self.growth = growth

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, "
              f"{self.s_age} days old")

    def grow(self) -> None:
        self.height += self.growth

    def age(self) -> None:
        self.s_age += 1


def main() -> None:
    print("=== Plant Factory Output ===")
    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Oak", 200, 365)
    plant3 = Plant("Cactus", 5, 90)
    plant4 = Plant("Sunflower", 80, 45)
    plant5 = Plant("Fern", 15, 120)
    print("Created: ", end="")
    plant1.show()
    print("Created: ", end="")
    plant2.show()
    print("Created: ", end="")
    plant3.show()
    print("Created: ", end="")
    plant4.show()
    print("Created: ", end="")
    plant5.show()


if __name__ == "__main__":
    main()
