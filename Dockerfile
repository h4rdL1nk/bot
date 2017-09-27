FROM alpine:3.6

ENV PACKAGES ca-certificates \
             bash \
             php7 \
             php7-openssl \
             php7-json \
             php7-phar \
             php7-iconv \
             php7-zlib


RUN apk update \
    && apk add ${PACKAGES} --no-cache \
    && mkdir -p /var/www/service

RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \
    && php -d memory_limit=16M composer-setup.php --install-dir=/usr/bin --filename=composer \
    && php -r "unlink('composer-setup.php');"

WORKDIR /var/www/service
ADD . ./
RUN composer require botman/botman botman/driver-slack