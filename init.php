<?php
require 'vendor/autoload.php';

use React\EventLoop\Factory;
use BotMan\BotMan\BotManFactory;
use BotMan\BotMan\Drivers\DriverManager;
use BotMan\Drivers\Slack\SlackRTMDriver;

// Load driver
DriverManager::loadDriver(SlackRTMDriver::class);

$loop = Factory::create();
$botman = BotManFactory::createForRTM([
    'slack' => [
        'token' => getenv('SLACK_BOT_TOKEN'),
    ],
], $loop);

$botman->hears('keyword', function($bot) {
    $bot->reply('I heard you! :)');
});

$botman->hears('convo', function($bot) {
    $bot->startConversation(new ExampleConversation());
});

$loop->run();