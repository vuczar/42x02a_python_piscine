class Plant():
    def __init__(
            self,
            name: str,
            s_height: float,
            s_age: int,
            growth: float = 0.8
            ) -> None:
        self.name = name
        self._height = 0.0
        self.set_height(s_height)
        self._s_age = 0
        self.set_age(s_age)
        self.growth = growth

    def show(self) -> None:
        print(f"{self.name}: {self._height:.1f}cm, "
              f"{self._s_age} days old")

    def grow(self) -> None:
        self._height += self.growth

    def age(self) -> None:
        self._s_age += 1

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._s_age

    def set_height(self, height: float) -> None:
        if (height < 0):
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
            return
        else:
            self._height = height

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
            return
        else:
            self._s_age = age


class Flower(Plant):
    def __init__(
            self,
            fname: str,
            fheight: float,
            fage: int,
            color: str
            ) -> None:
        super().__init__(fname, fheight, fage)
        self.color = color
        self.blooming = False

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if not self.blooming:
            print(f" {self.name} has not bloomed yet")
        else:
            print(f" {self.name} is blooming beautifully!")

    def bloom(self) -> None:
        self.blooming = True


class Tree(Plant):
    def __init__(
            self,
            tname: str,
            theight: float,
            tage: int,
            trunk_diameter: float
            ) -> None:
        super().__init__(tname, theight, tage)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"Tree {self.name} now produces a shade of "
              f"{self.get_height():.1f}cm long and "
              f"{self.trunk_diameter:.1f}cm wide.")

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter:.1f}cm")


class Vegetable(Plant):
    def __init__(
            self,
            vname: str,
            vheight: float,
            vage: int,
            harvest_season: str,
            growth: float = 0.8
            ) -> None:
        super().__init__(vname, vheight, vage, growth)
        self.harvest_season = harvest_season
        self.nutritional_value = 0.0

    def grow(self) -> None:
        super().grow()
        self.nutritional_value += 0.5

    def age(self) -> None:
        super().age()
        self.nutritional_value += 0.5

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value:.0f}")


def main() -> None:
    print("=== Garden Plant Types ===")
    print("=== Flower")
    plant1 = Flower("Rose", 15.0, 10, "red")
    plant1.show()
    print("[asking the rose to bloom]")
    plant1.bloom()
    plant1.show()
    print()
    print("=== Tree")
    plant2 = Tree("Oak", 200.0, 365, 5.0)
    plant2.show()
    print("[asking the oak to produce shade]")
    plant2.produce_shade()
    print()
    print("=== Vegetable")
    plant3 = Vegetable("Tomato", 5.0, 10, "April", 2.1)
    plant3.show()
    print("[make tomato grow and age for 20 days]")
    for _ in range(20):
        plant3.grow()
        plant3.age()
    plant3.show()


if __name__ == "__main__":
    main()
