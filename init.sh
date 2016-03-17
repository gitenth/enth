#!/usr/bin/env bash

#
#sudo pip3 install django
#sudo pip3 install gunicorn
#sudo apt-get install python3-dev libmysqlclient-dev
#sudo pip3 install mysqlclient 

#django-project  create
cd /home/box/web
django-admin startproject ask
sleep 2s
cd /home/box/web/ask
python manage.py startapp qa
sleep 2s

#templates
mkdir /home/box/web/ask/templates
cp /home/box/web/edit/templates/*  /home/box/web/ask/templates/

#ask_urls.py
rm /home/box/web/ask/ask/urls.py
cp /home/box/web/edit/ask_urls.py /home/box/web/ask/ask/urls.py

#settings.py
rm /home/box/web/ask/ask/settings.py
cp /home/box/web/edit/settings.py /home/box/web/ask/ask/

#qa_views.py
rm /home/box/web/ask/qa/views.py
cp /home/box/web/edit/qa_views.py /home/box/web/ask/qa/views.py

#qa_models.py
rm /home/box/web/ask/qa/models.py
cp /home/box/web/edit/qa_models.py /home/box/web/ask/qa/models.py

#qa_forms.py
rm /home/box/web/ask/qa/forms.py
cp /home/box/web/edit/qa_forms.py /home/box/web/ask/qa/forms.py

sleep 2s
#mysql - configuration
sudo /etc/init.d/mysql restart
sleep 5s
mysql -uroot -e "create database myproject;"
#mysql -uroot -e "CREATE USER 'enth'@'localhost' IDENTIFIED BY 'password';"
#mysql -uroot -e "GRANT ALL PRIVILEGES ON * . * TO 'enth'@'localhost';"
#mysql -uroot -e "FLUSH PRIVILEGES;"

#syncdb
python /home/box/web/ask/manage.py syncdb
sleep 5s

#nginx-settings
sudo rm /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sleep 5s

#gunicorn - settings
sudo ln -s /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
sudo /etc/init.d/gunicorn restart
sleep 5s

#gunicorn - start
cd /home/box/web/ask/ask
sudo gunicorn --bind 0.0.0.0:8080 ask.wsgi:application
#python /home/box/web/ask/manage.py runserver 0.0.0.0:8080


#там два каталога, sites-available, и sites-enabled, заходите в sites-available,
#копируете default в какой-то новый свой, там все удаляете и пишете что нужно,
#делаете символическую ссылку этого своего конфига в sites-enabled, удаляете из sites-enabled default,
#перезапускаете сервис
#netstat -tlnp проверить какие порты прослушиваются
#sudo apt-get install w3m
#w3m url текстовый браузер для диагностики проблем
