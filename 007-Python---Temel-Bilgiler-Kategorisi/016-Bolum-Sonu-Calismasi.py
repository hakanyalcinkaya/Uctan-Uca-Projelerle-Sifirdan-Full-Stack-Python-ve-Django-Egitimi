# Input ile first_name bilgisini al
# input ile last_name bilgisini al 
# input ile year_of_birth bilgisini al
# first_name ve last_name bilgilerinin karakter sayini yaz
# fString ile kullanicinin adinin ilk harfi ve buyuk olacak sekilde full_name yazdir
# yasini ve gelecek seneki yasini fString ile yazdir
# 18 yasindan buyukse True olacak sekilde bilgisini don



first_name = input("Adiniz: ")
last_name = input("Soyadiniz: ")
year_of_birth = input("Dogum Yiliniz: ")
print(f"Ad Karakter Sayisi: {len(first_name)}, Soyad Karakter Sayisi: {len(last_name)}")
# full_name = f"{first_name[0].upper()}. {last_name.upper()}"
full_name = f"{first_name[0]}. {last_name}".upper()
print(full_name)
print(f"Yasiniz: {2022 - int(year_of_birth)}, Gelecek Yil {(2022 +1) - int(year_of_birth)} Yasinda Olacaksiniz")  
# 2022'yi elle yaziyor olmak kesinlikle yanlis bir cozum.. muhakkak tarihin yil bilgi alinmaliydi ama 
# bu video hazirlanirken aslinda sen bunu bilmedigin icin cozum olarak elle yazdik ;)

print(f"Yasiniz 18'den Buyuk mu??? {(2022 - int(year_of_birth)) > 18}")
# Not: Bir Sonraki Bolumde bu bilgiler If ile tekrar gosterilecek..