#!/usr/bin/perl -w

push ( @program,'$i = 1;');
push ( @program,'$i = 3; $j = 2; $k = $i + $j');
push ( @program, '$i = 3; return 24; $k = $i + $j');

foreach $exp (@program)
{
    print "exp=[$exp]\n";
    $rtn =eval($exp);
    print $rtn,"\n";
}
