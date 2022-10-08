from curses.ascii import isdigit

age = input("Yasinizi Giriniz: ")

# Kullanici 18 Yasindan Buyuk mu?

# if age.isdigit() and int(age) > 18:
#     print("18 yasindan buyuk")
# else:
#     print("Verdiginiz bilgiler dogru degil veya 18 yasindan kucuksunuz")


if not age.isdigit():
    print('Yas Bilgisini Dogru Girmediniz')
else:
    if int(age) > 18:
        print("18 yasindan buyuk")
    else:
        print("18 yasindan kucuksunuz")


if age.isdigit():
    if int(age) > 18:
        print("18 yasindan buyuk")
    else:
        print("18 yasindan kucuksunuz")
else:
    print('Yas Bilgisini Dogru Girmediniz')


