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

    def bloom(self) -> None:
        pass


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

    def produce_shade(self):
        pass


class Vegetables(Plant):
    def __init__(
            self,
            vname: str,
            vheight: float,
            vage: int,
            harvest_season: str,
            nutritional_value: int
            ) -> None:
        super().__init__(vname, vheight, vage)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

def main() -> None:
    print("=== Garden Security System ===")
    print("Plant created: ", end="")
    plant1 = Plant("Rose", 15.0, 10)
    plant1.show()
    print()
    plant1.set_height(25.0)
    print(f"Height updated: {plant1.get_height():.0f}cm")
    plant1.set_age(31)
    print(f"Age updated: {plant1.get_age()} days")
    print()
    plant1.set_height(-26.0)
    plant1.set_age(-31)
    print()
    print("Current state: ", end="")
    plant1.show()


if __name__ == "__main__":
    main()
