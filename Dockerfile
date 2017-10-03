FROM alpine:3.6

ENV PACKAGES ca-certificates \
             tzdata \
             bash \
             apache2 \
             php7 \
             php7-apache2 \
             php7-openssl \
             php7-json \
             php7-phar \
             php7-iconv \
             php7-zlib

RUN rm /etc/localtime && ln -s /usr/share/zoneinfo/Europe/Madrid /etc/localtime
RUN apk update \
    && apk add ${PACKAGES} --no-cache \
    && mkdir -p /var/www/service

WORKDIR /var/www/service

RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \
    && php -d memory_limit=16M composer-setup.php --install-dir=/usr/bin --filename=composer \
    && php -r "unlink('composer-setup.php');"

ADD code/ ./
ADD entrypoint.sh /entrypoint.sh
ADD conf/httpd/ /etc/apache2/conf.d/

RUN composer install \
    && chown -R apache.apache /var/www/service \
    && chmod +x /entrypoint.sh

RUN mkdir -p /run/apache2

ENTRYPOINT ["/entrypoint.sh"]
CMD ["httpd","-D","FOREGROUND"]