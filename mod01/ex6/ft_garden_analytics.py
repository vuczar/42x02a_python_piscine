class Plant():

    class _Stats:
        def __init__(self) -> None:
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def add_grow(self) -> None:
            self._grow_calls += 1

        def add_age(self) -> None:
            self._age_calls += 1

        def add_show(self) -> None:
            self._show_calls += 1

        def display(self) -> None:
            print(f"Stats: {self._grow_calls} grow, "
                  f"{self._age_calls} age, {self._show_calls} show")

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
        self._stats = Plant._Stats()

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    def show(self) -> None:
        self._stats.add_show()
        print(f"{self.name}: {self._height:.1f}cm, "
              f"{self._s_age} days old")

    def grow(self, amount: float | None = None) -> None:
        self._stats.add_grow()
        if amount is None:
            amount = self.growth
        self._height += amount

    def age(self, days: int = 1) -> None:
        self._stats.add_age()
        self._s_age += days

    def display_stats(self) -> None:
        self._stats.display()

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

    @staticmethod
    def check_age(ages: int) -> bool:
        return ages > 365


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


class Seed(Flower):
    def __init__(
            self,
            sname: str,
            sheight: float,
            sage: int,
            color: str,
            seeds: int
            ) -> None:
        super().__init__(sname, sheight, sage, color)
        self._seed_capacity = seeds
        self.seeds = 0

    def bloom(self) -> None:
        super().bloom()
        self.seeds = self._seed_capacity

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self.seeds}")


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
        self._shade_calls = 0

    def produce_shade(self) -> None:
        self._shade_calls += 1
        print(f"Tree {self.name} now produces a shade of "
              f"{self.get_height():.1f}cm long and "
              f"{self.trunk_diameter:.1f}cm wide.")

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter:.1f}cm")

    def display_stats(self) -> None:
        super().display_stats()
        print(f" {self._shade_calls} shade")


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

    def grow(self, amount: float | None = None) -> None:
        super().grow(amount)
        self.nutritional_value += 0.5

    def age(self, days: int = 1) -> None:
        super().age(days)
        self.nutritional_value += 0.5

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value:.0f}")


def show_statistics(plant: Plant) -> None:
    print(f"[statistics for {plant.name}]")
    plant.display_stats()


def main() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old")
    days = 30
    print(f"Is {days} days more than a year? -> {Plant.check_age(days)}")
    days = 400
    print(f"Is {days} days more than a year? -> {Plant.check_age(days)}")
    print()

    print("=== Flower")
    plant1 = Flower("Rose", 15.0, 10, "red")
    plant1.show()
    show_statistics(plant1)
    print("[asking the rose to grow and bloom]")
    plant1.grow(8.0)
    plant1.bloom()
    plant1.show()
    show_statistics(plant1)
    print()

    print("=== Tree")
    plant2 = Tree("Oak", 200.0, 365, 5.0)
    plant2.show()
    show_statistics(plant2)
    print("[asking the oak to produce shade]")
    plant2.produce_shade()
    show_statistics(plant2)
    print()

    print("=== Seed")
    plant3 = Seed("Sunflower", 80.0, 45, "yellow", 42)
    plant3.show()
    print("[make sunflower grow, age and bloom]")
    plant3.grow(30.0)
    plant3.age(20)
    plant3.bloom()
    plant3.show()
    show_statistics(plant3)
    print()

    print("=== Anonymous")
    plant4 = Plant.anonymous()
    plant4.show()
    show_statistics(plant4)


if __name__ == "__main__":
    main()
