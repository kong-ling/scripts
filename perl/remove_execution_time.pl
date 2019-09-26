print "$0 is Processing $ARGV[0]";

open(FH, $ARGV[0]);
open(FH_OUTPUT, ">$ARGV[0]"."output");
while(<FH>)
{
    if (/(^\[\s*\d+\.\d+\])/)
    {
        print FH_OUTPUT $'
    }
    else
    {
        print FH_OUTPUT $_;
    }
}
