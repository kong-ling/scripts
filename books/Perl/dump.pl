
#!/usr/bin/perl

use strict;
use warnings;

use Data::Dumper;

my $a = "good";
my $b = "bad";
my @my_array = ("hello", "world", "123", 4.5);
my %some_hash = ("foo", 35, "bar", 12.4, 2.5, "hello",
          "wilma", 1.72e30, "betty", "bye\n");
##¿?¿?¿?¿?
print Dumper($a);
print Dumper(\@my_array);
print Dumper(\%some_hash);
print Dumper((\%some_hash, \@my_array));

