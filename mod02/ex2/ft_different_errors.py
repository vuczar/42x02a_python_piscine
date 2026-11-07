def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        10 / 0
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        "abc" + 1
    return


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    for number in range(5):
        print(f"Testing operation {number}...")
        try:
            garden_operations(number)
            print("Operation completed successfully")
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")

    print("\nCatching multiple types with one except...")
    for number in [0, 3]:
        try:
            garden_operations(number)
        except (ValueError, TypeError) as e:
            print(f"Caught a data error: {e}")

    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
