# fonksiyonlara gonderilen bilgilerin sayisi belli olmadan da kullanilabilir..

def user_info(user_name, password, *args, **kwargs):
    print(user_name, password)

    for item in args:
        print(item)
    print(kwargs)

user_info("Python", "Dj23q423423ango", 423423, 234523, 324,234, 23,4,234,23,4,23,432,4,23,4234, first_name="Denge", last_name="Duru")
