def input_temperature(temp_str: str) -> int:
    print(f"Input data is '{temp_str}'")
    temp_nbr = int(temp_str)
    print(f"Temperature is now {temp_nbr}°C")
    print()
    return temp_nbr


def test_temperature() -> None:
    try:
        input_temperature("25")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
        print()
    try:
        input_temperature("abc")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
        print()


if __name__ == "__main__":
    print("=== Garden Temperature ===")
    print()
    test_temperature()
    print("All tests completed - program didn't crash!")
