products = [
    ["laptop", "mouse", "keyboard", ["dip urun 1", "dip urun 2"]],
    ["monitor", "printer"],
    "Sony XYZ",
    "Beats Fit Pro",
    "Apple Magic Keyboard",
    "Logitech MX Master 3",
    12,
    23,
    34,
    True,
    False,
]

def print_items(items):
    for item in items:
        if not type(item) == list:
            print(item)
        else:
            print_items(item)

# print_items(products)

def flat_list(items, new_list=list()):
    for item in items:
        if not type(item) == list:
            new_list.append(item)
        else:
            flat_list(item, new_list)
    return new_list


new_items = flat_list(products)
print(new_items)