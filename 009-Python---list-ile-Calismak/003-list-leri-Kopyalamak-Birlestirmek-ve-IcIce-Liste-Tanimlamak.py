items = [
    "cable",
    "keyboard",
    "pc",
]

digital_products = ["laptop", "monitor", "mouse"]
other_products = ["lorem", "ipsum", "dolor"]

# new_items = [*items]
new_items = items.copy()
new_items[0] = "mic"

print("items", items)
print("new_items", new_items)

# items.append(digital_products)
# items.extend(digital_products)
items += digital_products + other_products

# items = items + digital_products + other_products
items = [
    *items, 
    *digital_products, 
    *other_products,
    1,
    2,
    3,
]
print("items", items)
# print(items[5])