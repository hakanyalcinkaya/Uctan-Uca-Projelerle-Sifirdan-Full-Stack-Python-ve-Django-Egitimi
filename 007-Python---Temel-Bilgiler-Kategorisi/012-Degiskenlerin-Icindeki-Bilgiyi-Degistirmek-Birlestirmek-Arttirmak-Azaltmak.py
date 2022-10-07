# Degisken Icindeki Bilgiyi Degistirmek
user_name = "lorem"
print(user_name)

# user_name = input("Adiniz: ")
user_name = "Degisti"
print(user_name)

# Degiskenler Icindeki Bilgileri Birlestirmek
first_name = "Hakan"
last_name = "Yalcinkaya"
full_name = first_name + last_name # Bosluk Yok
full_name = first_name + "" + last_name # Yine Bosluk Yok
full_name = first_name + " " + last_name

print(full_name)

# full_name = full_name + " Python"
full_name += " Python"
print(full_name)

# Degisken Icindeki Bilgiyi Arttirmak
age = 20
print(age)
age += 1
age += 10
print(age)

# Degisken Icindeki Bilgiyi Azaltmak
age -= 20
print(age)


age *= 20
print(age)

age /= 2
print(age)