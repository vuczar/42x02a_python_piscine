class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        Exception.__init__(self, message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        GardenError.__init__(self, message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        GardenError.__init__(self, message)


def check_plant(is_wilting: bool) -> None:
    if is_wilting:
        raise PlantError("The tomato plant is wilting!")


def check_water(water_level: int) -> None:
    if water_level < 10:
        raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===")

    print("\nTesting PlantError...")
    try:
        check_plant(True)
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("\nTesting WaterError...")
    try:
        check_water(5)
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("\nTesting catching all garden errors...")
    try:
        check_plant(True)
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        check_water(5)
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    print("\nTesting default messages...")
    for error in [GardenError(), PlantError(), WaterError()]:
        try:
            raise error
        except GardenError as e:
            print(f"Caught GardenError: {e}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
