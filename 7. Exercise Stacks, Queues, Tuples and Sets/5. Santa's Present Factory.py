from collections import deque

materials = deque(int(x) for x in input().split())
magic_levels = deque(int(x) for x in input().split())

crafted = []
presents = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle",
}

while materials and magic_levels:
    material = materials.pop() if magic_levels or not materials[0] else 0
    magic_level = magic_levels.popleft() if materials or not magic_levels[0] else 0

    if not magic_level:
        continue

    product = material * magic_level

    if presents.get(product):
        crafted.append(presents[product])
    elif product < 0:
        materials.append(material + magic_level)
    elif product > 0:
        materials.append(material + 15)

    if {"Doll", "Teddy bear"}.issubset(crafted) or {"Teddy bear", "Bicycle"}.issubset(crafted):
        pass