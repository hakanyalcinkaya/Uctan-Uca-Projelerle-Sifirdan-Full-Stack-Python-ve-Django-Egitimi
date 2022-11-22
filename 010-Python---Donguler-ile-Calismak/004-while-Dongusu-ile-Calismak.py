# kullanici ad bilgisini bildirene kadar devam et.. ve en az 5 karakter olsun
user = ""

while len(user) < 5:
    print("Lutfen kullanici adi 5 karakter veya daha fazla olsun..")
    user = input("Kullanici Adini Giriniz : ")
    print(user)


# kullanici ad ve soyad bilgisini bildirene kadar sormaya devam et..
first_name, last_name = "", ""
while len(first_name) < 5 and len(last_name) < 5:
    print("Lutfen kullanici adi 5 karakter veya daha fazla olsun..")
    first_name = input("Adiniz : ")
    last_name = input("Soyadiniz : ")

# kullanici ad veya soyad bilgisini bildirene kadar sormaya devam et..

first_name, last_name = "", ""
while len(first_name) < 5 or len(last_name) < 5:
    print("Lutfen kullanici adi 5 karakter veya daha fazla olsun..")
    first_name = input("Adiniz : ")
    last_name = input("Soyadiniz : ")