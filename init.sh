#!/usr/bin/env bash
mkdir /home/box/web/uploads

#nginx-settings
sudo rm /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart

#gunicorn - settings
sudo ln -s /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
sudo /etc/init.d/gunicorn restart

#django-project  create
cd /home/box/web
django-admin startproject ask
cd /home/box/web/ask
python manage.py startapp qa

#views.py
rm /home/box/web/ask/qa/views.py
cp /home/box/web/edit/views.py /home/box/web/ask/qa/

#urls.py
rm /home/box/web/ask/ask/urls.py
cp /home/box/web/edit/urls.py /home/box/web/ask/ask/

#settings.py
rm /home/box/web/ask/ask/settings.py
cp /home/box/web/edit/settings.py /home/box/web/ask/ask/

#model.py
rm /home/box/web/ask/qa/model.py
cp /home/box/web/edit/model.py /home/box/web/ask/qa/

#mysql - configuration
mysql -uroot -e "create database myproject;"
mysql -uroot -e "CREATE USER 'enth'@'localhost' IDENTIFIED BY PASSWORD 'waret1';"
mysql -uroot -e "GRANT ALL PRIVILEGES ON * . * TO 'enth'@'localhost';"
mysql -uroot -e "FLUSH PRIVILEGES;"

#syncdb
python /home/box/web/ask/manage.py syncdb

#gunicorn - start
cd /home/box/web/ask/ask
sudo (gunicorn --bind 0.0.0.0:8000 ask.wsgi:application &)


#там два каталога, sites-available, и sites-enabled, заходите в sites-available,
#копируете default в какой-то новый свой, там все удаляете и пишете что нужно,
#делаете символическую ссылку этого своего конфига в sites-enabled, удаляете из sites-enabled default,
#перезапускаете сервис
