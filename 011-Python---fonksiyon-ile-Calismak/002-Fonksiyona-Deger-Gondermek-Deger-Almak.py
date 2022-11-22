# fonksiyonlar bir veya birden daha fazla deger/parametre alabilir veya almayabilir..
# fonksiyonlara gonderilen parametreler default deger icerebilir..
# fonksiyonlar bir tip veri donebilir..
# fonksiyonlar tekrar kendilerini cagirabilirler..

def hello():
    return "Merhaba"
    # return ile bir bilgi donmedigi icin print icinde kullanamadik..



info = hello()
print(info)


def calc():
    2 * 2 
    return 100

calc_result = calc()

print(calc_result)



def greetings(name):
    print(f"{hello()} {name}")


greetings("Django")


def greetings_v2(first_name, last_name):
    return [first_name, last_name, ]

print(greetings_v2("Python", "Django"))


def greetings_v3(product, platform="Django"):
    print(product, platform)

greetings_v3("Dentorium")
greetings_v3("Doktorium", "Flask")

