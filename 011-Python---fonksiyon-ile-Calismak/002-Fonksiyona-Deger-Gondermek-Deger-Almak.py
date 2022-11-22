from random import randint
unique_ids = [0, 1, 2, 3, 4, 6, 7, 8, 9, 10]

def random_item():
    item = randint(0, 10)
    if item in unique_ids:
        return random_item()
    return item


products = [
    '',
    None,
    1,
    2,
    3,
    [4, 5,],
    6,
    [7, 8, 9,],
    10,
    11,
]

new_items = list()

for item in products:
    if item:
        if not type(item) == list:
            new_items.append(item)
        else:
            new_items += item    

print(new_items)

# def flat_item(items, flat_items=list()):
#     for item in items:
#         if item:
#             if not type(item) == list:
#                 flat_items.append(item)
#             else:
#                 flat_item(item, flat_items)
#     return flat_items


# print(flat_item(products))
