# https://pyformat.info/

first_name = "peLin"
last_name = "dJaNGo"

full_name = f"{first_name} {last_name}"

# Birden Fazla Degisken Icindeki Bilgiyi Birlestirmek
hello = "Merhaba " + first_name[0].upper() + ". " + last_name
print(hello)

# fString ile yazimi:
hello = f"Merhaba {first_name[0].upper()}. {last_name}"
print(hello)

# Hesaplama Yaparak str Sonuc Donmek
# print("Sonuc: " + 10 * 10) # Calismaz cunku str ve int birlesmez..
print("Sonuc: ", 10 * 10, sep="")
result = "Sonuc: 10 * 10"
result = "Sonuc: " + str(10 * 10)
print(result)

result = f"Sonuc: {10 * 10}"
print(result)

# function icinde yapilan hesaplamanin sonucunu donmek
def multiply(number):
    return number * number

result = f"Sonuc {multiply(10)}"
print("multiply fonksiyonu kullanildi:", result)

# uzun iceriklerin belli bir kismini gostermek
print(f"{result[:4]}")

# yazilari ortalamak veya saga yaslamak
print("*" * 30)
print(f"{full_name:-^30}")
print(f"{'Python':->30}")
print(f"{'Django':->30}")
print("*" * 30)

# belli bir uzunlukta int yapilar olusturmak: 000034 gibi
number = 34
print(f"{number:06d}")
