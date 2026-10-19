class Plant():
    name: str
    height: float
    time: int
    growth: float

    def grow(self) -> None:
        self.height += self.growth

    def age(self) -> None:
        self.time += 1

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.time} days old")


def main() -> None:
    plant = Plant()
    plant.name = "Rose"
    plant.height = 25.0
    plant.time = 30
    plant.growth = 0.8
    simulate_days = 7
    start_height = plant.height
    print("=== Garden Plant Growth ===")
    plant.show()
    for day in range(1, simulate_days + 1):
        print(f"=== Day {day} ===")
        plant.grow()
        plant.age()
        plant.show()
    print(f"Growth this week: {(plant.height - start_height):.1f}cm")


if __name__ == "__main__":
    main()
