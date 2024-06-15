import re

text = input()
valid_numbers = []

pattern = r"\d+"

while text:

    matches = re.findall(pattern, text)
    numbers = [str(match) for match in matches]

    for num in numbers:
        valid_numbers.append(num)

    text = input()

print(" ".join(valid_numbers))
