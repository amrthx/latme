<?php

spl_autoload_register($class)
{
    $file = $class . ".php";
    if(is_readable($file))
    {
        require $file;
    }
};
    $foo = new Foo();
    $foo->someFunction();

    $bar = new Bar();
    $bar->anotherFunction();
