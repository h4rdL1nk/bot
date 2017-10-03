#!/bin/sh

php /var/www/service/init.php &

exec "$@"