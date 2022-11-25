# - Django - Proje1:
## FAKE_DB ile Statik İçerikli Kurumsal Web Sitesi Projesi

### Projenin Amacı:
* Projenin hedefi birden fazla modül(App) ile Django projesi geliştirmek
* Django Template Language(DTL)'i anlamak
* Statik dosyalarla çalışmak
* DTL extends ile özelliğinin kullanımı
* DTL include ile modüler HTML yapısı oluşturmak
* Kendi Context Prosessor'ümüzü Oluşturup Proje Geneline Veri Göndermek
* URL yapısını anlamak
* SLUG ile çalışmak
* DB altyapısı kullanmadan Fake Data ile birden fazla detay sayfası ve ürün sayfası oluşturmak

## Kurulum
```shell
# TERMINAL:

# Windows Kullanicilari Icin:
pip install virtualenv
virtualenv proje1_venv  # proje icin sanal ortam olusturulmasi

# VirtualEnv Aktive Edilmesi:  PowerShell Kullaniliyorsa:
.\proje1_venv\Scripts\activate

# VirtualEnv Aktive Edilmesi:  Git Bash Kullaniliyorsa:
source proje1_venv/Scripts/activate

# ------------------------------------------

# Mac & Linux Kullanicilari Icin:
pip3 install virtualenv

virtualenv proje1_venv  # virtualenv --version diyerek ulasamiyorsaniz..
# Veya:
python3 -m virtualenv proje1_venv
source proje1_venv/bin/activate

# VirtualEnv aktif edildikten sonra:

pip install -r requirements.txt

# VirtualEnv'yi Deaktive Etmek Icin:
deactivate
```

## Projenin Çalıştırılması
```shell
# VirtualEnv Aktif Edildikten Sonra
python manage.py runserver
```

## SuperUser Olusturulmasi:
```shell
python manage.py createsuperuser
# NOT: Sifre girerken ekranda gozukmez.. Lutfen sifrenizi dogru girmeye ozen gosteriniz.
```

## SuperUser Sifresini Unutanlar icin :)
```shell
python manage.py changepassword kullanici_adi
# NOT: Kullanici Adini changepassword un hemen yanina yazmaniz gerekiyor.. eger yazmazsaniz sistem kullanici adinin sifresini degistirmek istediginizi Django varsayar(default behavior).
```

## Katkıda Bulunmak:
Aldığınız notları ve insanların işine yarayacağını düşündüğünüz bilgileri ekleyebilirsiniz. Böylelikle bu repo içerisinde sizinde isminiz geçer ve birçok kişiye destek olabilirsiniz. Başarılar dilerim 🔥