# Toplama Cikarma
print(2 + 2)
print(3 + -2)

# Carpma Bolme
print(2 * 10)
print(3 / 2) # Python3: Sonuc 1.5, Python2: Sonuc 1 // Neden ? Python3 Bolmede Float, Python2 Bolmede Int doner..
print("3 / 3:::", type(3 / 3))
print("3 * 3:::", type(3 * 3))

# Islem Onceligi ve Parantez Kullanimi
# print(2 + 8 * 5) -> 50 cikmadi :)))
print( (2 + 8) * 5 ) 

# Kalansiz Bolme (Int)
print(3 / 3)
print("3 / 3:::", type(3 / 3))

print(3 // 3)
print("3 // 3:::", type(3 // 3))
print(4 // 3)

# Mod Alma (Kalani Bulma) 
print("Kalan Nedir? ", 9 % 3 )
print("Kalan Nedir? ", 20 % 6 )
print(20 // 6 ) # Kalansiz Bolmeyi Her Kolinin icinde 6 urun oldugunu dusunup kac koli kullanabilecegimizi bulmak icin kullandik

# Kalansiz Bolme ve Kalani Bulma :) / divmod
print("divmod'u goster")
print( divmod(20, 6) ) 
