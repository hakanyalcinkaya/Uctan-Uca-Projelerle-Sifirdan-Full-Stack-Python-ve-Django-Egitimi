users = [
    "Cigdem",
    "Aytug",
    "Derin",
    "Derya",
    "Berk",
]

# continue
for item in range(10):
    if item == 5:
        continue
    print(item)


print("-" * 30)

# break
for item in range(10):
    if item == 5:
        break
    print(item)

print("-" * 30)

for user in users:
    if user == "Derin":
        continue
    print(user)

print("-" * 30)

for user in users:
    if user == "Derin":
        break
    print(user)