user_info = ["admin", "123234sdfsdzwa23", ]
user, password = user_info
# print(user_info[0], user_info[1])
# print(user, password)

user_detail = ["admin", "123234sdfsdzwa23", "admin@admin.com", "mail-master@admin.com", ]

user_name, user_password, *mail_list = user_detail

print(user_name, user_password, mail_list)

products = [
    ["laptop", "mouse", "keyboard"],
    ["monitor", "printer"],
    "Sony XYZ",
]

*other_products, headphone = products 

print("other_products", other_products)
print("headphone", headphone)

# liste icindeki verileri tek tek islemek
users = ["Aysen", "Fatma", "Cigdem", "Hasan", "Ahmet", "Mehmet"]

#  item ve index bilgisi ile listleri dongude kullanmak -> enumerate
for index, user in enumerate(users):
    if index % 2 != 0:
        print(index, user)