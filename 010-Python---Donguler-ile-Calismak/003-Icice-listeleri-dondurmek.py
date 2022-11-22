products = [
    ["laptop", "mouse", "keyboard"],
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
    (1, 2, 3,),
]

for item in products:
    if type(item) == list:
        for pr in item:
            print(pr)
    elif type(item) == str:
        print(item)