import re

def add(numbers: str) -> int:
    if numbers == "":
        return 0
    delimiter = ",|\n"
    if numbers.startswith("//"):
        parts = numbers.split("\n", 1)
        delimiter_part = parts[0][2:]
        numbers = parts[1]

    if delimiter_part.startswith("[") and delimiter_part.endswith("]"):
        delimiters = re.findall(r"\[(.*?)\]", delimiter_part)
        delimiter = "|".join(map(re.escape, delimiters))
    else:
        delimiter = re.escape(delimiter_part)
    
    number_list = re.split(delimiter, numbers)
    int_numbers = []
    negative_numbers = []

    for num in number_list:
        if num.strip():
            n = int(num)
            if n < 0:
                negative_numbers.append(n)
            elif n <= 1000:     
                int_numbers.append(n)

    if negative_numbers:
        raise ValueError(f"negative numbers not allowed {', '.join(map(str, negative_numbers))}")

    return sum(int_numbers)
