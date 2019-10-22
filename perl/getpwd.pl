#! /usr/bin/perl

# /home/lte_ip.work/lingkong/xg748_es1_latest_hw/bwcSwFefcProcFft_para_pfifo_01_level1/case_001
my $cur_dir = `pwd`;
my $cur_user = `whoami`;
my $cur_proj;
chomp($cur_dir);
chomp($cur_user);
print "cur_dir  = $cur_dir\n";
print "cur_user = $cur_user\n";

#                                  user        proj   test   case
$cur_dir =~ /home\/lte_ip\.work\/(\w+)\/(\w+)\/(\w+)\/(\w+)/;
#my $user     = $1;
#my $proj     = $2;
#my $test     = $3;
#my $testcase = $4;
my ($user, $proj, $test, $testcase) = ($1, $2, $3, $4);
my $cur_subcomp;
print "user     =  $user\n";
print "proj     =  $proj\n";
print "test     =  $test\n";
print "testcase =  $testcase\n";

$proj =~ /(\w+)_latest_hw/;
my $proj_version = $1;

if ($proj_version eq "xg748_es1")
{
}
elsif ($proj_version eq "xg748_es2")
{
}
elsif ($proj_version eq "xg746_es1")
{
    $proj_version = "xg756_a0";
}
elsif ($proj_version eq "xg756a0_es1")
{
    $proj_version = "xg756_a0";
}
elsif ($proj_version eq "xg756b0_es1")
{
    $proj_version = "xg756_b0";
}
else
{
    die "New projects! please adapt asap\n";
}


my $path_in_lte_hw_cv = '/vobs/lte_ip_testcases/test/src/lte_hw_cv/'."$proj_version\/$proj\/$test\/$testcase";
print "path_in_lte_hw_cv = $path_in_lte_hw_cv \n";
