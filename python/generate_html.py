import re
import os
import string

html_header = '''
DOCTYPE html>
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

html_tail = '''
    <body>
        <h3><a href="xg756_es2_latest_hw_gen.html">Results</a></h3>
        <!--jenkins begin-->
        <pre>Chip:   xg756 es2</pre>
        <pre>Branch: latest</pre>
        <pre>Target: HW level 1</pre>
        <pre>Start:  06-Mar-2017 18:40:40</pre>
        <pre>End:    06-Mar-2017 18:44:03</pre>
        <pre>-</pre>
        <table>
            <tr>
                <th rowspan="2">Subcomp</th>
                <th rowspan="2">Test entry</th>
                <th colspan="2" style="text-align:center;">Number of tests</th>
            </tr>
            <tr>
                <th style="width:80px;text-align:center;">Total</th>
                <th style="width:80px;text-align:center;">Failed gen</th>
            </tr>
            <tr>
                <td rowspan="1">FEFC</td>
                <td><a href="#T001">bwcSwFefcProcFft_para:01</a></td>
                <td style="text-align:center;">001</td>
                <td style="text-align:center;"><span class="pass">000</span></td>
            </tr>
            <tr>
                <td colspan="2">Grand total</td>
                <td style="text-align:center;">001</td>
                <td style="text-align:center;"><span class="pass">000</span></td>
            </tr>
        </table>
        <!--jenkins end-->
        <h3>Detailed results</h3>
        <h4>bwcSwFefcProcFft_para:01</h4>
        <table id="T001">
            <tr>
                <th rowspan="2" style="width:80px;">TestCases</th>
                <th rowspan="2" style="width:65px;">Gen verdict</th>
                <th colspan="2" style="text-align:center;">Gen duration</th>
                <th colspan="2" style="text-align:center;">Job info</th>
            </tr>
            <tr>
                <th style="width:50px;text-align:center;">XML gen</th>
                <th style="width:50px;text-align:center;">XML cnv</th>
                <th style="width:30px;text-align:center;">Log</th>
                <th style="width:150px;text-align:center;">Scheduling</th>
            </tr>
            <tr>
                <td style="width:90px;"><a href="bwcSwFefcProcFft_para_01_level1/cases_001_step001_011">1:1:11</a></td>
                <td><span class="pass">PASS</span></td>
                <td style="text-align:center;">00m01s</td>
                <td style="text-align:center;">00m03s</td>
                <td style="text-align:center;"><a href=".xg756_es2_latest_hw_gen_jobs/log1.txt">0001</a></td>
                <td style="padding:0px"><div style="background-color:SeaShell"><div style="background-color:LightSalmon;left:0.0%;width:100.0%;position:relative;">&nbsp;</div></div></td>
            </tr>
            <tr>
                <td style="width:90px;"><a href="bwcSwFefcProcFft_para_01_level1/cases_001_step001_0002">1:1:11</a></td>
                <td><span class="pass">PASS</span></td>
                <td style="text-align:center;">00m01s</td>
                <td style="text-align:center;">00m03s</td>
                <td style="text-align:center;"><a href=".xg756_es2_latest_hw_gen_jobs/log1.txt">0001</a></td>
                <td style="padding:0px"><div style="background-color:SeaShell"><div style="background-color:LightSalmon;left:0.0%;width:100.0%;position:relative;">&nbsp;</div></div></td>
            </tr>
        </table>
    </body>
</html>
'''

html_file = open('test.html', 'w')

file_list = os.popen('find . -name "*.txt" | xargs ls | xargs grep Result')
info = file_list.readlines()
for line in info:
    line = line.strip('\r\n')

    #./647/bwcSwSystemRx_paraPdcchOnly_01_level1/reports_lingkong/case_001__2017-05-31_07_30_05.txt:Result: PASS
    #pattern = re.compile(r'^\.\/(\d+)\/(\w+)\/(\w+)\/(.+\.txt):Result:\ (\w+)')
    compiled_pattern = re.compile(r'^\.\/(\d+)\/(\w+)\/(\w+)\/(.+\.txt):Result:\ (\w+)')

    match = compiled_pattern.match(line)
    if match:
        print match.groups()

    print line

html_file.write(html_header)
html_file.write(html_tail)
html_file.close()
