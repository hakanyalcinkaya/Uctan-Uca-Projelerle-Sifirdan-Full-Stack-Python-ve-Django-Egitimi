# yeni dict(dictionary) nasil olusturulur?
# dict icindeki verilere nasil erisilir
# olan veri nasil degistirilir ?
# yeni veri nasil eklenir ?


car = {
    0: "Bu Sifirinci Bilgi :)))",
    "brand": "Pego",
    "model": "3008",
    "stock": 3,
    "price": 100,
}

print(car[0])
print(car["price"])
car["max_speed"] = 200

print(car)

car["max_speed"] = 250
car["stock"] = 2
print(car)
