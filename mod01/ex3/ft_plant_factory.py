class Plant():
    def __init__(self, name: str, s_height: float, s_age: int):
        self.name = name
        self.s_height = s_height
        self.s_age = s_age

    def show(self) -> None:
        print(f"Created: {self.name}: {self.s_height:.1f}cm, "
              f"{self.s_age} days old")


def main() -> None:
    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Oak", 200, 365)
    plant3 = Plant("Cactus", 5, 90)
    plant4 = Plant("Sunflower", 80, 45)
    plant5 = Plant("Fern", 15, 120)
    print("=== Plant Factory Output ===")
    plant1.show()
    plant2.show()
    plant3.show()
    plant4.show()
    plant5.show()


if __name__ == "__main__":
    main()
