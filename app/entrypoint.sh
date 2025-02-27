#!/bin/bash

/etc/init.d/mysql start
sleep 5

mysql -u root -e "CREATE USER IF NOT EXISTS 'hitesh'@'localhost' IDENTIFIED BY 'hitesh';"
mysql -u root -e "GRANT ALL PRIVILEGES ON *.* TO 'hitesh'@'localhost' WITH GRANT OPTION;"
mysql -u root -e "FLUSH PRIVILEGES;"

exec /home/ubuntu/phonebook/bin/python3 /home/ubuntu/phonebook/app.py
