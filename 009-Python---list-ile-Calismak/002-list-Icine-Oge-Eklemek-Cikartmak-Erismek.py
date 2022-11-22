# list Icindeki Ogelere Erismek
first_item, second_item, third_item = "first", "second", "third"

items = [
    first_item, 
    second_item,
    third_item,
]

print(items)
print(items[0])
print(items[1])

# list Icine Yeni Oge Eklemek
fourth_item = 'fourth'
items.append(fourth_item)
items.append('fifth')
items.append(1)
print(items)


# list Icindeki Ogenin Icindeki Bilgiyi Degistirmek
print(len(items))
items[len(items) -1] = 'sonuncu oge'
items[-1] = 'gercekten sonuncu oge..'
print(items)

# list Icinde Belli Bir Yere Oge Eklemek
items.insert(3, "yeni oge")
items.insert(0, "en basa eklenen oge")
# ensona insert ile ekle ;)
items.insert(len(items), 'en sonnnn..')
print(items)

# list Icindeki Belli Bir Bolumu Listelemek
print(items[2:5])
print(items[2:])

# list'in ilk 3 Ogesi
print(items[:3])

# list'in son 3 Ogesi
print(items[len(items) -3 :])

# list'i Terse Cevir
print(items[::-1])
print(items)  # degismemis eger degismesini istersen esitlemeyi unutma.. 
# items = items[::-1]

# Son Ogeye Ulas
print(items[-1])

# STEP belirleyerek bilgileri al.. 1, 3, 5
step_items = items[::2]
print(step_items)
