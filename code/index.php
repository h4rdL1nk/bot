<?php

require 'vendor/autoload.php';

$app = new \Slim\Slim();

$app->group('/api', function ($req, $res) {
	$this->get('/test', function ($req, $res) {
		$body = "Test API";
		$modres = $res->withStatus(200)
					  ->withHeader("Content-Type","application/json")
					  ->write($body);

		return $modres;
	});
});


$app->run();

?>