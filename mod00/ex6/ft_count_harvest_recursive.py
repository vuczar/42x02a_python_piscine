def ft_recursive(days):
    if days > 1:
        ft_recursive(days - 1)
    print(f"Day {days}")


def ft_count_harvest_recursive():
    x = int(input("Days until harvest: "))
    ft_recursive(x)
    print("Harvest time!")
