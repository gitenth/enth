#!/usr/bin/env bash
mkdir /home/box/web/uploads
sudo rm /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo cp /home/box/web/etc/nginx.conf /etc/nginx/sites-available/default
sudo ln -sf /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart