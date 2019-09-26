my @testResult = `find -name "*.txt" | xargs ls -rt | xargs grep "Result: " | cat -n`;

foreach (@testResult)
{
    # ./bwcSwSystemRx_paraCa_03_level1/reports_lingkong/case_113__2017-10-04_02_41_30.txt:Result: PASS
    if(/(\w+)\/(\w+)\/(\w+__\d{4}-\d{2}-\d{2}_\d{2}_\d{2}_\d{2})\.txt:Result: PASS/)
    {
        my $testLog = join '/', $1, $2.'_run', $3;
        #print "$testLog\n";
        #my $failInfo = `tail -C 100 $testLog`;
        print;
        #print "failInfo --> $failInfo\n";
    }

    if(/(\w+)\/(\w+)\/(\w+__\d{4}-\d{2}-\d{2}_\d{2}_\d{2}_\d{2})\.txt:Result: FAIL/)
    {
        my $testLog = join '/', $1, $2.'_run', $3;
        my $failInfo = `tail -n 20 $testLog`;
        print;
        print "log file: $testLog\n";
        print "failInfo:\n$failInfo\n";
    }

    print "=====================================================================\n";
}
