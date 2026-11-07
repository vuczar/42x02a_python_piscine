import sys


def parse_inventory(args: list[str]) -> dict[str, int]:
    inventory: dict[str, int] = {}
    for arg in args:
        try:
            name, quantity = arg.split(":")
        except ValueError:
            print(f"Error - invalid parameter '{arg}'")
            continue
        if name in inventory:
            print(f"Redundant item '{name}' - discarding")
            continue
        try:
            value = int(quantity)
            if value < 0:
                raise ValueError("quantity can't be negative")
        except ValueError as e:
            print(f"Quantity error for '{name}': {e}")
            continue
        inventory.update({name: value})
    return inventory


def main() -> None:
    print("=== Inventory System Analysis ===")
    inventory = parse_inventory(sys.argv[1:])
    if len(inventory) == 0:
        print("Inventory is empty. Usage: "
              f"python3 {sys.argv[0]} <item>:<quantity> ...")
        return

    print(f"Got inventory: {inventory}")
    items = list(inventory.keys())
    print(f"Item list: {items}")
    total = sum(inventory.values())
    print(f"Total quantity of the {len(items)} items: {total}")

    if total > 0:
        for item in items:
            percent = round(inventory[item] / total * 100, 1)
            print(f"Item {item} represents {percent}%")

    most = items[0]
    least = items[0]
    for item in items:
        if inventory[item] > inventory[most]:
            most = item
        if inventory[item] < inventory[least]:
            least = item
    print(f"Item most abundant: {most} with quantity {inventory[most]}")
    print(f"Item least abundant: {least} with quantity {inventory[least]}")

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
