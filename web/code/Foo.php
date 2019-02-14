<?php

class Foo
{
    public function someFunction()
    {
        echo "Calling ". __FUNCTION__ ."() inc class ". __CLASS__ ."\n";
    }
}
