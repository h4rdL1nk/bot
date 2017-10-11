<?php

require 'vendor/autoload.php';

$app = new \Slim\Slim();


$app->get('/', function ($req, $res, $args) {

    $data = [
                "string" => "Load-balancer health check OK",
            ];

    $body = json_encode($data,JSON_PRETTY_PRINT|JSON_UNESCAPED_SLASHES);
    $modres = $res->withStatus(200)
                  ->withHeader("Content-Type","application/json")
                  ->write($body);

    return $modres;

});

$app->get('/util/rand/string', function ($req, $res, $args) {

	$length = 20;
    $keyspace = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';

    $str = '';
    $max = mb_strlen($keyspace, '8bit') - 1;
    if ($max < 1) {
        throw new Exception('$keyspace must be at least two characters long');
    }
    for ($i = 0; $i < $length; ++$i) {
        $str .= $keyspace[random_int(0, $max)];
    }

    $data = [
                "string" => $str,
            ];

    $body = json_encode($data,JSON_PRETTY_PRINT|JSON_UNESCAPED_SLASHES);
    $modres = $res->withStatus(200)
                  ->withHeader("Content-Type","application/json")
                  ->write($body);

    return $modres;
    
});	

$app->run();