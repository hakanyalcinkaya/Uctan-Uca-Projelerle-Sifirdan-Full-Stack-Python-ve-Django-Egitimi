# tuple nedir ? 
# tuple nasil tanimlanir ? 
# list ile farki nedir
# len kullanimi
# tuple'a veri nasil eklenir/eklenebilir mi ?
# tuple'dan veri nasil silinir/silinebilir mi ?

SERVER_INFO = ("user12w4353", "fidsfoierofihersoifgherih")


print(SERVER_INFO)
print(len(SERVER_INFO))

for item in SERVER_INFO:
    print(item)


user = ("Derya", "Django", [1, 2, 3,], {"age": 18, "gender": "f"})

user[2].append(100)
user[3]["lang"] = "Python"

del(user[3]["gender"])

print(user[2])
print(user[3])

# del(user[1])