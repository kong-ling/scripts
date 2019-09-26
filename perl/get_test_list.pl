@test_result = `grep "Result: [FAIL|PASS]" * | cat -n`;

my @pass_list;
my @fail_list;

foreach (@test_result)
{
    #print;
   
    #    52  case_086__2017-10-17_05_29_39.txt:Result: FAIL
    if (/(\d+)\s+case_(\d{3})__(\d{4}-\d{2}-\d{2}_\d{2}_\d{2}_\d{2})\.txt:Result:\s+(\w+)/)
    #if (/(\d+)\s+case_(\d{3})__(\d{4}-\d{2}-\d{2}_\d{2}_\d{2}_\d{2})/)
    {
        my $caseNumber = $2;
        my $runTime    = $3;
        my $verdict    = $4;
        #print "$caseNumber $runTime $verdict\n";

        if ($verdict ~= /PASS/)
        {
            $
        }
        

    }
}
