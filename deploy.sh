#!/usr/bin/env bash

cp cowsay.service /usr/lib/systemd/system/cowsay.service
systemctl daemon-reload
systemctl restart cowsay

cp cowsay.tbmh.org.conf /etc/nginx/conf.d/cowsay.tbmh.org.conf
nginx -t
systemctl reload nginx
