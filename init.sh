#!/usr/bin/env bash
mkdir /home/box/web/uploads
sudo cp /etc/nginx/sites-available/default default
sudo rm /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default
sudo cp ./etc/nginx.conf /etc/nginx/sites-available/default
sudo ln -sf /etc/nginx/sites-available/default /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart

#там два каталога, sites-available, и sites-enabled, заходите в sites-available,
#копируете default в какой-то новый свой, там все удаляете и пишете что нужно,
#делаете символическую ссылку этого своего конфига в sites-enabled, удаляете из sites-enabled default,
#перезапускаете сервис nginx