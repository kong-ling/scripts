function testlist = update_testlist(se_phy_mainline_or_not)
    %update the test list by lteDispHwTest
    testlist = sprintf('%s/testlist.txt', getenv('workAlgorithms'));
    if exist(testlist, 'file') == 2 %file exist, then delete and create a new one
        system(sprintf('rm -fv %s', testlist));
    end

    fprintf(sprintf('Generating %s', testlist));
    diary(testlist);
    lteDispHwTests;
    diary off;

end
