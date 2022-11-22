# list icine list Eklemek
users = []

user_1 = ["Ayse", 1234]
user_2 = ["Hasan", 12344556]

users.append(user_1)
users.append(user_2)

print(users)

products = [
    ["laptop", "mouse", "keyboard"],
    ["monitor", "printer"],
    "headphone",
]


# list icindeki list'e Erismek

print(products)

print(products[2]) 

print(users[1])


# list icindeki list'i Silmek

first_user = users.pop(0)

print("first_user:", first_user)
print("users:", users)


print("products:", type(products))
print("products 0. Oge", type(products[0]))
print("products 2. Oge", type(products[2]))