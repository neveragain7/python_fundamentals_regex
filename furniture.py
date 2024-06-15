import re

text = input()
pattern = r"^>>(?P<furniture_name>[A-za-z]+)<<(?P<price>\d+[\.\d]*)!(?P<quantity>\d+)$"
furniture = []
final_price = 0

while not text == "Purchase":

    matches = re.finditer(pattern, text)

    for match in matches:
        furniture_name = match.group("furniture_name")
        price = float(match.group("price"))
        quantity = int(match.group("quantity"))
        total_price = price * quantity
        final_price += total_price

        furniture.append(furniture_name)
    text = input()


print("Bought furniture:")
for item in furniture:
    print(item)

print(f"Total money spend: {final_price:.2f}")
