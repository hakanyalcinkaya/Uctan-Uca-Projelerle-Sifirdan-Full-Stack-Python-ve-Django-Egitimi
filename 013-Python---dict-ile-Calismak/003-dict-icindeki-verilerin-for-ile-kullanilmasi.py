# for ile anahtarlar nasil cagirilir
# for ile degerler nasil cagirilir
# for ile anahtar ve degerler nasil cagirilir

car = {
    "brand": "Pego",
    "model": "3008",
    "stock": 3,
    "price": 100,
}

for key in car:
    print(key) # keys..
    # key bilgisini kullanarak value bilgisine ulasalim..
    print(car[key])


print(" - " * 30)

for key in car.keys():
    print(car[key])

print(" - " * 30)

for item in car.values():
    print(item)


print(" - " * 30)
for key, item in car.items():
    print(key, item)

