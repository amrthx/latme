<?php

/*function __autoload($class)
{
    $file = $class . ".php";
    if(is_readable($file))
    {
        require $file;
    }

    $foo = new Foo();
    $foo->someFunction();

    $bar = new Bar();
    $bar->anotherFunction();
}*/
include('Foo.php');
include('Bar.php');

$foo = new Foo();
$foo->someFunction();

$bar = new Bar();
$bar->anotherFunction();
?>
