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
             php7-zlib \
             php7-dom \
             php7-tokenizer \
             php7-mbstring \
             php7-curl \
             php7-ctype

RUN rm /etc/localtime && ln -s /usr/share/zoneinfo/Europe/Madrid /etc/localtime
RUN apk update \
    && apk add ${PACKAGES} --no-cache \
    && mkdir -p /var/www/service

WORKDIR /var/www/service

RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \
    && php -d memory_limit=16M composer-setup.php --install-dir=/usr/bin --filename=composer \
    && php -r "unlink('composer-setup.php');"

RUN ln -s /dev/stdout /var/log/apache2/access.log \
    ln -s /dev/stderr /var/log/apache2/error.log

ADD code/ ./
ADD tests/ ./tests
ADD entrypoint.sh /entrypoint.sh
ADD conf/httpd/httpd.conf /etc/apache2/
ADD conf/httpd/service.conf /etc/apache2/conf.d/
ADD conf/httpd/modules.conf /etc/apache2/conf.d/

RUN composer install \
    && chown -R apache.apache /var/www/service \
    && chmod +x /entrypoint.sh

RUN mkdir -p /run/apache2

ENTRYPOINT ["/entrypoint.sh"]
CMD ["httpd","-D","FOREGROUND"]