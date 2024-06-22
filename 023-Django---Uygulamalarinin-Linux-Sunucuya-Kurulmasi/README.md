# Ubuntu Server Üzerinde Birden Fazla Django Projesinin NGINX, uWSGI ve PostgreSQL ile Kurulumu

**Not:** [Projelerle Django Eğitimi](http://lnk.ktlzr.co/pddj) serisinde projelerimizi yayına almak için 2 farklı bölüm hazırladım. Aşağıdaki dökümantasyon kurulumu zor olan Linux sunuculara terminal ile bağlanarak yapabileceğiniz bir kurulum yöntemidir. Bu yöntemi öğrenmeden önce DigitalOcean'ın App Platform yöntemi ile Django projelerinizi kurmayı öğrenmenizi tavsiye ederim.

> Bu dökümantasyon, Ubuntu sunucusu üzerinde birden fazla Django projesinin NGINX, uWSGI ve PostgreSQL ile nasıl kurulacağını adım adım anlatmaktadır.

> Projelerin isimleri firstsite ve secondsite olarak belirlenmiştir.

## SSH ile Sunucuya Bağlanın
```bash
ssh username@server_ip 
# Not: -p ile port belirtebilirsiniz. Default port 22 olduğu için belirtmenize gerek ama portu değiştirdiyseniz sunucuya bağlanmak için doğru porttan bağlandığınıza emin olun..

# Örnek: ssh root@10.10.10.10 -p 2121 
```


## Gerekli Paketlerin Güncellenmesi ve Kurulması

### Öncelikle superuser (root) moduna geçin:
```bash
sudo su -
# Şifrenizi yazmayı unutmayın ;)
```


> Not: eğer root kullanıcısı olarak sistemde isteniz # işaretini bulunduğunuz path bilgisinin sonunda görmeniz gerekmektedir.

> Örnek:
>> root@ubuntu-server:/var/www#

### Paketleri Güncelleyin
```bash
apt update
```

### NGINX ve pip3 Kurulumu
```bash
apt install python3-pip nginx python3-dev
```

### virtualenv ve virtualenvwrapper kurun:
```bash
pip3 install virtualenv virtualenvwrapper uwsgi --break-system-packages
```

## Sanal Ortamların Ayarlanması

### virtualenvwrapper.sh script dosyasını bulun:
Eğer virtualenvwrapper dosyasının yolunu ve script dosyasını bulamazsanız başka bir klasörde olabilir. Bu yüzden dosyasının .bashrc'ye eklenmeden önce yerinin doğru olduğunu kontrol etmek önemli.
```bash
ls /usr/local/bin/virtualenvwrapper.sh
```

### Aşağıdaki satırları .bashrc dosyanıza ekleyerek virtualenvwrapper yapılandırmasını yapın:
```bash
echo "export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3" >> ~/.bashrc
echo "export WORKON_HOME=~/Env" >> ~/.bashrc
echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc
echo 'alias www="cd /var/www"' >> ~/.bashrc
```

#### Bonus: Alternatif .bashrc Dosyasına Ekleme Yöntemi: 
**Not:** Bu işlem yukardaki işlemin alternatifidir :) Bonus yazdım ama olsun Not olarak eklemekte fayda var ;)
```bash
{
    echo "export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3"
    echo "export WORKON_HOME=~/Env"
    echo "source /usr/local/bin/virtualenvwrapper.sh"
    echo 'alias www="cd /var/www"' 
} >> ~/.bashrc
```

### Yapılandırma değişikliklerini yüklemek için .bashrc dosyasını yeniden yükleyin:
```bash
source ~/.bashrc
```

## Django Projelerinin Oluşturulması
```bash
cd /var/www
# veya daha önceden tanımladığımız
# alias olan
# www 
# kısayolunu da kullanabilirsiniz ;)
# cd /var/www yerine www yazıp enter tuşuna basarak her zaman /var/www klasörüne ulaşabilirsiniz.. Bu tür kısayollar oluşturmak ilerde işinize yarayabilir.
```

### İlk sanal ortamı oluşturun ve Django kurun:
```bash
mkvirtualenv firstsite
pip install django
django-admin startproject firstsite
deactivate
```

### İkinci sanal ortamı oluşturun ve Django kurun:
```bash
mkvirtualenv secondsite
pip install django
django-admin startproject secondsite
deactivate
```

## uWSGI'yi Test Etme
uWSGI'nin doğru çalıştığını doğrulamak için aşağıdaki komutu çalıştırın:

```bash
uwsgi --http :8080 --home /root/Env/firstsite --chdir /var/www/firstsite -w firstsite.wsgi
```

> Kullandığınız Browser'a gidip belirttiğiniz port ile bağlantı kurmayı deneyin. Eğer belirttiğiniz port ile bağlantı yaptıysanız uWSGI çalışıyor ve NGINX ile bağlantı yapılabilir anlamına gelmektedir.

## uWSGI Yapılandırması
uWSGI yapılandırma dosyalarını oluşturun:

### Birinci proje için yapılandırma:
```bash
mkdir -p /etc/uwsgi/sites

nano /etc/uwsgi/sites/firstsite.ini
```

nano text editörü üzerinden açtığınız dosyanın içeriği

/etc/uwsgi/sites/firstsite.ini
```
[uwsgi]
project = firstsite
uid = root
base = /%(uid)
www = /var/www

chdir = %(www)/%(project)
home = %(base)/Env/%(project)
module = %(project).wsgi:application

master = true
processes = 5

socket = /run/uwsgi/%(project).sock
chown-socket = www-data:www-data
chmod-socket = 660
vacuum = true
```

### İkinci proje için benzer yapılandırmayı yapın:

```bash
nano /etc/uwsgi/sites/secondsite.ini
```

/etc/uwsgi/sites/secondsite.ini dosyasının içeriği
```
[uwsgi]
project = secondsite
uid = root
base = /%(uid)
www = /var/www

chdir = %(www)/%(project)
home = %(base)/Env/%(project)
module = %(project).wsgi:application

master = true
processes = 5

socket = /run/uwsgi/%(project).sock
chown-socket = www-data:www-data
chmod-socket = 660
vacuum = true
```

### uWSGI Servis Dosyasının Oluşturulması
#### uWSGI servis dosyasını oluşturun:

```bash
nano /etc/systemd/system/uwsgi.service
```

İçeriği:
```
[Unit]
Description=uWSGI Emperor service

[Service]
ExecStartPre=/bin/bash -c 'mkdir -p /run/uwsgi; chown www-data:www-data /run/uwsgi'
ExecStart=/usr/local/bin/uwsgi --emperor /etc/uwsgi/sites
Restart=always
KillSignal=SIGQUIT
Type=notify
NotifyAccess=all

[Install]
WantedBy=multi-user.target
```

## NGINX Yapılandırması
### İlk Site İçin NGINX Yapılandırması

```bash
nano /etc/nginx/sites-available/firstsite
```

İçeriği:
```
server {
    listen 80;
    server_name firstsite.com www.firstsite.com;

    location = /favicon.ico { access_log off; log_not_found off; }
    
    location /static/ {
        root /var/www/firstsite;
    }

    location /media/ {
        root /var/www/firstsite;
    }

    location / {
        include         uwsgi_params;
        uwsgi_pass      unix:/run/uwsgi/firstsite.sock;
    }
}
```

### İkinci Site İçin NGINX Yapılandırması
```bash
nano /etc/nginx/sites-available/secondsite
```

İçeriği: 
```
server {
    listen 80;
    server_name secondsite.com www.secondsite.com;

    location = /favicon.ico { access_log off; log_not_found off; }
    
    location /static/ {
        root /var/www/secondsite;
    }

    location /media/ {
        root /var/www/secondsite;
    }

    location / {
        include         uwsgi_params;
        uwsgi_pass      unix:/run/uwsgi/secondsite.sock;
    }
}
```

### Siteleri Etkinleştirmek
NGINX yapılandırma dosyalarını etkinleştirin:

```bash
ln -s /etc/nginx/sites-available/firstsite /etc/nginx/sites-enabled/
ln -s /etc/nginx/sites-available/secondsite /etc/nginx/sites-enabled/
```
**Not**: NGINX içerisinde **sites-available** klasörü kullanılabilir web site ayarlarının tutulduğu yerdir. **sites-enabled** klasörü ise aktif olan web sitelerinin ayarlarının bulunduğu klasördür. 

### NGINX yapılandırmasını test edin:
```bash
nginx -t
```

## Hizmetlerin Başlatılması ve Etkinleştirilmesi
```bash
systemctl start uwsgi
systemctl restart nginx
```

### uWSGI hizmet durumunu kontrol edin:
```bash
systemctl status uwsgi
```

### Hizmet günlüklerini kontrol edin:
```bash
journalctl -u uwsgi
```

### Servislerin Aktif Hale Getirilmesi
```bash
systemctl enable nginx
systemctl enable uwsgi
```
### Artık Servisleri Restart Edeblir veya Durdurup Başlatabiliriz..
```bash
# Servis Durdurma
service uwsgi stop

# Servis Başlatma
service uwsgi start

# Servis Restart
service uwsgi restart

# Aynı İşlemleri Diğer Servisler için de uygulayabilirsiniz.
```

## PostgreSQL Kurulumu ve Yapılandırması
Gerekli PostgreSQL paketlerini kurun:

```bash
apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib -y
```

PostgreSQL kullanıcı moduna geçin:
```bash
sudo -i -u postgres
# giriş yaptığınızda:
# postgres@ubuntu-server:~$ olarak görünecek
```

PostgreSQL shell'e girin:
```bash
psql
```

```bash
# CREATE ROLE user_name WITH LOGIN SUPERUSER;
CREATE ROLE root WITH LOGIN SUPERUSER;

# Çıkış:
\q
```

PostgreSQL Kullanıcısındandan çıkın:
```bash

exit
```

Tekrar root kullanıcısına döndüğünüzde root için veritabanı ekleyin
```bash
createdb
```

Artık psql shell'e bağlanırken sudo -i -u postgres ile postgres kullanıcısıan geçiş yapmanıza gerek yok..
```bash
psql
```

Yeni bir kullanıcı ve veritabanı oluşturun:
```sql
# PSQL Shell:
CREATE USER project_user WITH PASSWORD 'xxxxxx';
CREATE DATABASE project_db OWNER project_user;
```

Veritabanı listesini kontrol edin:
```bash
\l
```

Django ve PostgreSQL Entegrasyonu
```bash
workon firstsite
pip install psycopg2 python-dotenv
```

### .env dosyanızı düzenleyin:
```bash
nano /var/www/firstsite/.env
```

Aşağıdaki bilgileri projenize göre düzenleyin..
```bash
DEBUG = True
DB_DEBUG = False
SECRET = "secretkey_bilgisi"
DB_NAME = "database_name"
DB_USER = "db_username"
DB_PASSWORD = "db_password"
```

firstsite için **settings.py** dosyasına aşağıdaki bilgileri ekleyin:

> Not: settings.py dosyasının yolunu biliyor ve nano ile veya herhangi bir text editorü ile açtığınızı varsayıyorum..
> 
```python
from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET")

DEBUG = os.getenv("DEBUG", "False") == "True"
DB_DEBUG = os.getenv("DB_DEBUG", "False") == "True"

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

if DEBUG:
    print("x" * 30)
    print(f"{DEBUG = }")
    print("x" * 30)

if not DB_DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': DB_NAME,
            'USER': DB_USER,
            'PASSWORD': DB_PASSWORD,
            'HOST': 'localhost',
            # 'PORT': '',
        }
    }

STATIC_URL = 'static/'

STATIC_ROOT = BASE_DIR / 'static/'

STATICFILES_DIRS = [
    BASE_DIR / "static_files",
]

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media/'
```

Aynı işlemleri **secondsite** için yaparak projenizi düzenleyin.

### .py Dosyasında Değişiklik Yaptıktan Sonra uwsgi Servisinin Restart Edilmesi Gerekmektedir.
```bash
service uwsgi restart
```

## Bonus:
Sık yaptığız işlemleri alias olarak .bashrc dosyasına veya .bash_profile veya .zshrc dosyasına ekleyebilirsiniz.
```bash
{
    alias ..="cd ../"
    alias ...="cd ../../"
    alias dj="python manage.py"
    alias uwr="service uwsgi restart"
    alias lsa="ls -lah"
} >> ~/.bashrc
```
