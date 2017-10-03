$app = new \Slim\App();

$app->group('/api', function ($req, $res, $args) {
	$this->get('/test', function ($req, $res, $args) {
		$body = "Test API";
		$modres = $res->withStatus(200)
					  ->withHeader("Content-Type","application/json")
					  ->write($body);

		return $modres;
	});
});


$app->run();

?>