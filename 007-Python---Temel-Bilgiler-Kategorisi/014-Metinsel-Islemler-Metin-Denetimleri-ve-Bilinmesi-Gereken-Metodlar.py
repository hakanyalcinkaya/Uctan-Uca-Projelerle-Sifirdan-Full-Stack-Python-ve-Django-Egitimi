first_name = "peLin"
last_name = "dJaNGo"
user_name = "123456789"

# str'nin ilk karakteri [0]
print(first_name[0])
print(last_name[1])

# belli bir yerden baslayan bilgiyi goster [3:10]
print(first_name[2:4])

# bastan 3 karakter [:3]
print(first_name[:3])

# sonran 3 karakter [-3:]
print(first_name[-3:])

# son 3 karakteri gosterme [:-3]
print(user_name[:-3])

# ter cevir [::-1]
print(user_name[::-1])

# Tumu Buyuk Harf Olsun -> upper
full_name = first_name + " " + last_name
print(full_name.upper())

# Ilk Harfi Buyuk Olsun -> capitalize
print(full_name.capitalize())

# Ilk Harfleri Buyuk Olsun -> title
print(full_name.title())

# Ters Cevir -> swapcase
print(full_name.swapcase())

# Kucuk Harf Olsun -> lower
print(full_name.lower())

# say -> count
print(full_name.lower().count('n'))

# liste icindekileri birlestir -> join
names = ["Pelin", "Cem", "Bilge", "Deniz", ]
print(", ".join(names))

# parcala / ayir -> split
print(full_name.split(" "))

# SOR:::

# baslik seklinde mi? istitle
print("Django".istitle())
print(last_name.istitle())

# hepsi kucuk harf mi? islower
print("pelin".islower())
print(first_name.islower())

# print(input("Adiniz Yaz: ").islower())

# belli bir karakterle basliyor mu? startswith
print("belli bir karakterle basliyor mu? startswith", first_name.startswith("p"))

# belli bir karakterle bitiyor mu? endswith
print("belli bir karakterle bitiyor mu? endswith", first_name.endswith("p"))

# aradigim bilgi str icinde var mi? find
print(user_name.find("3"))
print(user_name[user_name.find("7"):])

print(full_name[full_name.lower().find("n"):])

# belli bir bilgiyi degistir? replace
print(full_name.replace("peLin", "Python"))