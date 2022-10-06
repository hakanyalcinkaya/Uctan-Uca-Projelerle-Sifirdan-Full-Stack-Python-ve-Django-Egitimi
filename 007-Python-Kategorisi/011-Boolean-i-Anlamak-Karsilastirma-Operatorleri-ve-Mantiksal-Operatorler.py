# Icinde Bilgi Var mi?
# "lorem"
# 10
# -10
# 0
username = ""
print(bool(username))

age = 10
print(bool(age))

# Yas Esit mi 0'a?

age = 0
print(bool(age == 0))

# Yas Esit Degildir 0'a
age = 25
print(age != 0)
print(not age == 0)

# Yasi 18'den Buyuk mu?
print( age > 18 )

# Yasi 18'den Kucuk mu?
print( age < 18 )

# Yasi 18'den Buyuk veya Esit mi?
print( age >= 18 )

# Yas Bilgisi 20 ila 30 Arasinda mi ?
age = 25
print(20 < age < 30)

# Yasi 18den Buyuk mu veya Kadin mi? OR Kullanimi
gender = "f"
age = 10
print("Yasi 18den Buyuk mu veya Kadin mi? OR Kullanimi", age > 18 or gender == 'f')

# Yasi 18den Buyuk mu ve Kullanici Bilgisi Var mi?
username = ""
age = 20
print("Yasi 18den Buyuk mu ve Kullanici Bilgisi Var mi?", age > 18 and bool(username))
print("Yasi 18den Buyuk mu ve Kullanici Bilgisi Var mi?", age > 18 and username != "")
print("Yasi 18den Buyuk mu ve Kullanici Bilgisi Var mi?", age > 18 and not username == "")

username = "lorem"
print("Yasi 18den Buyuk mu ve Kullanici Bilgisi Var mi?", age > 18 and bool(username))