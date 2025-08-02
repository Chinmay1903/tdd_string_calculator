def add(numbers: str) -> int:
    if numbers == "":
        return 0
    # Assuming the input is a comma-separated string of numbers
    numbers = numbers.split(",")
    return sum(int(n) for n in numbers)