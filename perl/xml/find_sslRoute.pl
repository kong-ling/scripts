printf("Processing %s\n", $ARGV[0]);
open(FH, $ARGV[0]);
while (<FH>)
{
    if (/\<sslRoute\>/)
    {
        while (<FH>)
        {
            unless (/sslRoute\>/)
            {
                print;
            }
        }
    }
}
