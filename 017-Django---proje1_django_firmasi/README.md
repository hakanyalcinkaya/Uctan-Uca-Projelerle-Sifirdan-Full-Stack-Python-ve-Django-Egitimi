# **Django** Proje1:
## FAKE_DB ile Statik İçerikli Kurumsal Web Sitesi Projesi

### Projenin Amaçları:
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

## Projelere Katkıda Bulunabilirsiniz ve/veya README Dosyasının Daha Detaylı Hale Gelmesine Katkıda Bulunabilirsiniz
Aldığınız notları ve insanların işine yarayacağını düşündüğünüz bilgileri ekleyebilirsiniz. Böylelikle bu repo içerisinde sizinde isminiz geçer ve birçok kişiye destek olabilirsiniz. Başarılar dilerim 🔥

```
.
├── README.md
├── db.sqlite3
├── django_firmasi
│   ├── __init__.py
│   ├── asgi.py
│   ├── project_context_processors.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── page
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── fake_db
│   │   └── pages.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── templates
│   │   └── page
│   │       ├── components
│   │       │   ├── hero_component.html
│   │       │   └── home_carousel.html
│   │       ├── deleted
│   │       │   ├── about_us.html
│   │       │   ├── contact_us.html
│   │       │   └── vision.html
│   │       ├── home_page.html
│   │       └── page_detail.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── product
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── fake_db
│   │   └── products.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── templates
│   │   └── product
│   │       ├── components
│   │       │   └── card.html
│   │       ├── product_detail.html
│   │       └── products.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── requirements.txt
├── static_files
│   ├── css
│   │   └── bootstrap.min.css
│   └── js
│       └── bootstrap.bundle.min.js
├── templates
│   └── core
│       ├── base.html
│       ├── footer.html
│       ├── navbar.html
│       └── projects.html
```