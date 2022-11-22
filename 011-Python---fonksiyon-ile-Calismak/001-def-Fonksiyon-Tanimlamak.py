# fonksiyonlar def ile tanimlanir
# fonksiyonlar bir veya birden daha fazla deger/parametre alabilir veya almayabilir..
# fonksiyonlara gonderilen parametreler default deger icerebilir..
# fonksiyonlar bir tip veri donebilir.. (return)
# fonksiyonlar tekrar kendilerini cagirabilirler..
# fonksiyonlara gonderilen bilgilerin sayisi belli olmadan da kullanilabilir..

def hello():
    print("Merhaba")

hello() # calistirmis olduk..


name = "Derya"

def greetings():
    # global degisken bilgisini kullanabilir ama cooook riskli..
    print(f"Merhaba {name}")

greetings()

print("Öldük mü??")