use XML::Simple;
use Data::Dumper;

print "$0 is parsing $ARGV[0]\n";

#$xml = XMLin('sample.xml');
$xml = XMLin($ARGV[0], ForceArray => 1);
print Dumper($xml);

#$xml_hash = Dumper($xml);
#print "xml_hash = [$xml_hash]\n";

#foreach $key (keys $xml)
#{
#    #print "$key => $($xml){$key}\n";
#    print "xxxx: $key\n";
#}

print "xml->text is $xml->{topicref}[0]->{topicref}[0]->{href}\n";
print "xml->user is $xml->{id}\n";;

for (my $i = 0; $i <= 8; $i++)
{
    print "xml->topicref is $xml->{topicref}[0]->{topicref}[$i]->{href}\n";
}
