function varargout = lte_do_test(What, TestListFile, TestEntryArray, merged_or_not, dryRun)
    Gen = strcmp(upper(What),'GEN');
    Run = strcmp(upper(What),'RUN');

    if Gen
        target_cmd = 'Gen';
    end

    if Run
        target_cmd = 'Run';
    end

    lineNumber = 1;
    fid = fopen(TestListFile, 'r');
    while ~feof(fid)
        testLine = fgetl(fid); 

        lineNumber = lineNumber + 1;

        %parse the test case and test entry
        testDetail = strsplit(testLine, '|');

        try
            testIndex   = str2num(testDetail{1, 2});
            subComp     = testDetail{1, 3};
            testEntry   = testDetail{1, 4};
            testLevel   = testDetail{1, 5};
            testComment = testDetail{1, 7};

            if testIndex% IDX is number

                % test entry is empty, all entries will be proceed
                if ( isempty(TestEntryArray)  || find(TestEntryArray == testIndex) ) % only specified test entries will be proceeded
                    try

                        %if merged mode is tageted, use 0 as test case number
                        if strcmp(merged_or_not, 'merged')
                            testCases   = '0';
                            cmd = sprintf('lte%sHwTest(%3d, %10s); %%%s', target_cmd, testIndex, testCases, testEntry);
                        else
                            testCases   = strrep(strtrim(testDetail{1, 6}), 'merged', ''); %replace 'merged' with ''
                            cmd = sprintf('do_test(''%s'', %d, %s); %%%s', target_cmd, testIndex, testCases, testEntry);
                        end

                        fprintf('cmd = %s\n', cmd);
                        if (dryRun == 0)
                            eval(cmd);
                        end
                    catch
                        fprintf(lasterr);
                    end
                end
            else
                continue
            end;
        catch
            %fprintf(lasterr);
        end;
        %celldisp(testDetail);
    end;
end

function do_test(What, testEntry, testcases)
% specify the test entry, and testcases
% gen_test(
    for i= testcases
        try
            fprintf('run %d=> %d test\n', testEntry, i);
            cmd = sprintf('lte%sHwTest(testEntry, i)', What);
            fprintf('cmd = %s\n', cmd);
            eval(cmd);
        catch
            fprintf('%d: %s\n', i, lasterr);
        end
    end
end
