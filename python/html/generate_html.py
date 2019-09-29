#####################################################################
## generate report in html format
## testlist should be provided, 
## otherwise, $(workAlgorithms/testlist.txt will be used
#####################################################################

import re
import os
import string
import datetime
import sys

#import user defined module
import analyze_path

currentDir  = os.getcwd()
currentTime = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")

#usage
if len(sys.argv) < 2 :
    print 'Usage:'
    print 'python %s testlist' % currentDir
    print 'if testlist is missing, the default will be usd\n'
    testlist = '%s/testlist.txt' % os.getenv('workAlgorithms') #the default testlist
else:
    testlist = sys.argv[1] #the second is testlist


#print cli arguments
for i in range(len(sys.argv)):
    print 'argv[%s] = %s' % (i, sys.argv[i])


print "At %s Executing %s\nFrom path:%5s\n" % (currentTime, __file__, currentDir)

html_header = '''
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html;charset=utf-8">
        <title>Report</title>
        <style type="text/css">
        body, p
        {
            font-family:Neo Sans Intel, Calibri, sans-serif;
        }
        
        h3, h4
        {
            font-family:Neo Sans Intel, Calibri, sans-serif;
            font-weight:bold;
        }
        
        h3
        {
            font-size:1.5em;
            margin-bottom:0.5em;
        }
        
        h4
        {
            font-size:0.8em;
            margin-bottom:0.2em;
        }
        
        pre
        {
            margin-top:0.0em;
            margin-bottom:0.0em;
        }
        
        table
        {
            border-collapse:collapse;
            margin-top:0.0em;
            margin-bottom:1.0em;
        }
        
        table, td, th
        {
            font-family:Neo Sans Intel, Calibri, sans-serif;
            border:1px solid DarkCyan;
            text-align:left;
            vertical-align:middle;
        }
        
        td, th 
        {
            font-size:0.75em;
            padding:0px 5px;
            margin-bottom:0.0em;
        }
        
        th 
        {
            color:#FFFFFF;
            background-color:CadetBlue;
            font-weight:bold;
        }
        
        .pass {
            color:LimeGreen;
            font-weight:bold;
        }
        .fail {
            color:Red;
            font-weight:bold;
        }
        
        a:link {text-decoration:none;}
        a:visited {text-decoration:none;}
        a:hover {text-decoration:underline;}
        a:active {text-decoration:underline;}
        
        /*a:hover {background:#ffffff; text-decoration:none;} /*BG color is a must for IE6*/
        a.tooltip_err  {color:Red;}
        a.tooltip_err span {display:none; padding:5px; margin-left:20px; width:auto; text-align:left; font-family:monospace; color:Red; text-decoration:none; z-index:1; position:absolute; background:#ffffcc}
        a.tooltip_err:hover span {display:block}
        
        a.tooltip_info {color:Blue;}
        a.tooltip_info span {display:none; padding:5px; margin-left:20px; width:auto; text-align:left; font-family:monospace; color:Blue; text-decoration:none; z-index:1; position:absolute; background:#ffffcc}
        a.tooltip_info:hover span {display:block}
                </style>
            </head>
'''
#print html_header

html_body_temp = '''
    <body>
        <h3><a href="xg732.html">Results</a></h3>
        <!--jenkins begin-->
        <pre>Chip:   xg732 es1</pre>
        <pre>Branch: latest</pre>
        <pre>Target: HW level 1</pre>
        <pre>-</pre>
        <!--jenkins end-->
'''
## parse /p/libdev/lte_ip.work2/lingkong/xg732_es1_latest_hw
result_path = currentDir.split('/')
#print result_path

html_body = '''
    <body>
        <h3><a href="%s">Results</a></h3>
        <pre>CurDir:   %s</pre>
        <pre>testlist: %s</pre>
        <pre>Branch:   latest</pre>
        <pre>Target:   HW level 1</pre>
        <pre>Run Time: %s</pre>
        <pre>-</pre>
''' % (currentDir, currentDir, result_path[7], currentTime)

#print html_body

html_tail = '''
    </body>
</html>
'''
table_head = '''
        <table id="myTable" data-role="table" data-mode="columntoggle" class="ui-responsive ui-shadow" data-filter="true" data-input="#filterTable-input">
            <tr>
                <th rowspan="2" style="width:10px;">Index</th>
                <th rowspan="2" style="width:80px;">TestEntry</th>
                <th rowspan="2" style="width:150px;">TestCases</th>
                <th rowspan="2" style="width:150px;">Test</th>
                <th rowspan="2" style="width:150px;">RunTime</th>
                <th rowspan="2" style="width:80px;">xtRiscTb.m</th>
                <th rowspan="2" style="width:80px;">Result</th>
                <th rowspan="2" style="width:65px;">Tester Name</th>
                <th rowspan="2" style="width:65px;">Run Log</th>
            </tr>
            <tr>
            </tr>
'''
table_tail = '''
        </table>
'''

func_for_search = '''
<script>
    function myFunction() {
      var input, filter, table, tr, td, i;
      input = document.getElementById("myInput");
      filter = input.value.toUpperCase();
      table = document.getElementById("myTable");
      tr = table.getElementsByTagName("tr");
      for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[0];
        if (td) {
          if (td.innerHTML.toUpperCase().indexOf(filter) > -1) {
            tr[i].style.display = "";
          } else {
            tr[i].style.display = "none";
          }
        }       
      }
    }
</script>
'''

search_input = '''
        <h2>My Filter</h2>
        <input type="text" id="myInput" onkeyup="myFunction()" placeholder="Search for names..." title="Type in a name">
'''

########################################################################
#
#  get testEntry and test from analyze_path
#
########################################################################

tests = analyze_path.get_test_info_from_testlist_split(testlist)
items = tests.items()

########################################################################
#
#  generate the html for reporting
#
########################################################################
html_file = open('test_%s.html' % currentTime, 'w')
html_file.write('<!DOCTYPE html>')
html_file.write(html_header)
html_file.write(html_body)
html_file.write(search_input)
html_file.write(table_head)

#testEntry_index     = 1
#testEntry_name      = 2
#test_report_folder  = 3
#test_report_name    = 4
#test_verdict        = 5
TEST_INDEX          = 0
TEST_ENTRY_NAME     = 1
TEST_REPORT_FOLDER  = 2
TEST_REPORT_NAME    = 3
TEST_CASE           = 3
TEST_NUMBER         = 4
TEST_TIME           = 5
TEST_VERDICT        = 4

indent_4  = '    '
indent_8  = '%s%s' % (indent_4, indent_4)
indent_12 = '%s%s' % (indent_8, indent_4)
indent_16 = '%s%s' % (indent_8, indent_8)


file_list = os.popen('find . -name "*.txt" | xargs ls | xargs grep Result')
#print file_list.read()
info = file_list.readlines()
for line in info:
    line = line.strip('\r\n')

    ##just for debugging
    #print line

    #./647/bwcSwSystemRx_paraPdcchOnly_01_level1/reports_lingkong/case_001__2017-05-31_07_30_05.txt:Result: PASS
    pattern = re.compile(r'\.\/(\w+)\/(\w+)\/(case.+)\.txt:Result:\ (\w+)')

    match = pattern.match(line)
    if match:

        ##################################
        ## print out the matches
        ##################################
        #print match.groups()

        test_index         = match.group(TEST_INDEX)
        test_entry         = match.group(TEST_ENTRY_NAME)
        test_report_folder = match.group(TEST_REPORT_FOLDER)
        #test_report_name   = match.group(TEST_CASE) + '_' + match.group(TEST_NUMBER)+ '__' + match.group(TEST_TIME)
        test_report_name   = match.group(TEST_REPORT_NAME)
        test_verdict       = match.group(TEST_VERDICT)

        testcase    = test_report_name.split('__')
        tester_name = test_report_folder.split('_')
        
        #print out report and user
        #print tester_name

        html_file.write('%s<tr>\n' % indent_12)
        #html_file.write('    <td style="width:90px;"><a href="bwcSwFefcProcFft_para_01_level1/cases_001_step001_000x">1:1:11</a></td>\n')

        try:
            html_file.write('%s<td style="width:90px;"><a href="./%s">%s</a></td>\n' % (indent_16, test_index, tests[test_entry][1]))
            html_file.write('%s<td style="width:90px;"><a href="./%s">%s</a></td>\n' % (indent_16, test_entry, test_entry))
            html_file.write('%s<td style="width:90px;"> %s</td>\n' % (indent_16, tests[test_entry][5]))
        except:
            html_file.write('%s<td style="width:90px;"><a href="./%s">%s</a></td>\n' % (indent_16, test_index, '?'))
            html_file.write('%s<td style="width:90px;"><a href="./%s">%s</a></td>\n' % (indent_16, test_entry, test_entry))
            html_file.write('%s<td style="width:90px;"> %s</td>\n' % (indent_16, 'MissingIdx'))
        
        html_file.write('%s<td style="width:90px;"><a href="./%s/%s/%s.txt">%s</a></td>\n' % (indent_16, test_entry, test_report_folder, test_report_name, testcase[0]))
        html_file.write('%s<td style="width:90px;">%s</td>\n' % (indent_16, testcase[1]))
        html_file.write('%s<td style="width:90px;"><a href="./%s/%s/%s">xtRiscTb.m</a></td>\n' % (indent_16, test_entry, testcase[0], 'xtRiscTb.m'))

        if test_verdict == 'PASS':
            html_file.write('%s<td><span class="pass">%s</span></td>\n' % (indent_16, test_verdict))
        else:
            html_file.write('%s<td><span class="fail">%s</span></td>\n' % (indent_16, test_verdict))
        
        #html_file.write('\t\t\t\t<td style="text-align:center;">-</td>\n')
        html_file.write('%s<td style="text-align:center;">%s</td>\n' % (indent_16, tester_name[1]))

        html_file.write('%s<td style="width:90px;"><a href="./%s/%s_run/%s">run_log</a></td>\n' % (indent_16, test_entry, test_report_folder, test_report_name))
        html_file.write('%s</tr>\n' % indent_12)

        #print match.group(1)
        #print match.group(3)
    else:
        print 'no match found...'
html_file.write(table_tail)

html_file.write(func_for_search)

html_file.write(html_tail)
html_file.close()
