# bir anahtar var mi nasil kontrol edilir

car = {
    0: "Bu Sifirinci Bilgi :)))",
    "brand": "Pego",
    "model": "3008",
    "stock": 3,
    "price": 100,
}

# print(car['olmayan_anahtar_bilgisi'])


print(car.get("olmayan_anahtar_bilgisi", "bu olabilir.."))

print("onemli bisey calisiyor..")