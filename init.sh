#!/usr/bin/env bash
mkdir /home/box/web/uploads
sudo rm /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo ln -s /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
sudo /etc/init.d/gunicorn restart
#sudo gunicorn -b 0.0.0.0:8080 hello:application
cd /home/box/web
django-admin startproject ask
cd /home/box/web/ask
python manage.py startapp qa
rm /home/box/web/ask/qa/views.py
cp /home/box/web/views.py /home/box/web/ask/qa/
rm /home/box/web/ask/ask/urls.py
cp /home/box/web/urls.py /home/box/web/ask/ask/
cd /home/box/web/ask/ask
sudo (gunicorn --bind 0.0.0.0:8000 ask.wsgi:application &)


#там два каталога, sites-available, и sites-enabled, заходите в sites-available,
#копируете default в какой-то новый свой, там все удаляете и пишете что нужно,
#делаете символическую ссылку этого своего конфига в sites-enabled, удаляете из sites-enabled default,
#перезапускаете сервис
