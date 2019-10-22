# find the failed test cases
my $failed_test_list = `find -name "*.txt" | xargs ls | xargs grep "Result: FAIL" | cat -n`;

print "failed_test_list=\n[$failed_test_list]\n";

#split the file list and save to array
my @files_list = split '\n', $failed_test_list;

#use to save the test case number
my @cases_no;
my $test_count = 0;

foreach (sort @files_list)
{
    $test_count ++;
    #print "test_count = $test_count ";
    #print;
    /case_(\d{3})/;
    #print "-> case number: $1\n";
    
    # push test case number to array
    push @cases_no, sprintf("%d", $1);
}

my $sTestList = "";

foreach (@cases_no)
{
    $sTestList .= "$_ ";
}

#print out the test list for rerun or regenerate
print "sTestList = $sTestList\n";
