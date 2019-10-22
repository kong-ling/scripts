use XML::Simple;
use Data::Dumper;

print "$0 is parsing $ARGV[0]\n";

$xml = XMLin($ARGV[0], ForceArray => 1);

## just for debug
#print Dumper($xml);

my @entries = $xml->{row}[0];
#print($xml->{row}, "\n");
#print($xml->{row}[0], "\n");
#print($xml->{row}[1], "\n");
#print($xml->{row}[0]->{entry}, "\n");
#print($xml->{row}[0]->{entry}[0], "\n");

$ssl_count = scalar(@{$xml->{row}});

printf("xmlns              is %20s\n", $xml->{xmlns});
printf("xmlns:xsi          is %20s\n", $xml->{"xmlns:xsi"});
printf("xsi:schemaLocation is %20s\n", $xml->{"xsi:schemaLocation"});

#dump entry information
#for (my $i = 0; $i <= scalar(@entries); $i ++)
for (my $i = 0; $i < $ssl_count; $i ++)
{
    printf("row[$i] is %20s, %20s, %20s\n", $xml->{row}[$i]->{entry}[0], $xml->{row}[$i]->{entry}[1],  $xml->{row}[$i]->{entry}[2]);
}
