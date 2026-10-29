def input_temperature(temp_str: str) -> int:
    print(f"Input data is '{temp_str}'")
    temp_nbr = int(temp_str)
    if temp_nbr > 40:
        raise ValueError(f"{temp_nbr}°C is too hot for plants (max 40°C)")
    if temp_nbr < 0:
        raise ValueError(f"{temp_nbr}°C is too cold for plants (min 0°C)")
    print(f"Temperature is now {temp_nbr}°C")
    print()
    return temp_nbr


def test_temperature() -> None:
    inputs = ["25", "abc", "100", "-50"]
    for temp_str in inputs:
        try:
            input_temperature(temp_str)
        except ValueError as e:
            print(f"Caught input_temperature error: {e}")
            print()


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===")
    print()
    test_temperature()
    print("All tests completed - program didn't crash!")
