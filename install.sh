#!/bin/bash

if ["$EUID" -ne 0]
	then echo "Please re-run using the sudo command."
else
	sudo apt-get update
	sudo apt-get install apache2
	sudo apt-get install php5 libapache2-mod-php5 php5-mcrypt
	sudo apt-get upgrade apache2 php5
	sudo chown -R $USER /var/www/*
	python gui.py
fi