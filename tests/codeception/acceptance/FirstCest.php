<?php


class FirstCest
{
    public function _before(AcceptanceTester $I)
    {
    }

    public function _after(AcceptanceTester $I)
    {
    }

    // tests
    public function tryToTest(AcceptanceTester $I)
    {
	$I->amOnPage('/mail/log/6DE78420E3');
	$I->see('6DE78420E3');
    }
}
