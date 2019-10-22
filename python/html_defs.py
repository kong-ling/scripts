HTML_HEADER = '''
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

HTML_BODY_TEMP = '''
    <body>
        <h3><a href="xg732.html">Results</a></h3>
        <!--jenkins begin-->
        <pre>Chip:   xg732 es1</pre>
        <pre>Branch: latest</pre>
        <pre>Target: HW level 1</pre>
        <pre>-</pre>
        <!--jenkins end-->
'''

#print html_body

HTML_TAIL = '''
    </body>
</html>
'''
TABLE_HEAD = '''
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
TABLE_TAIL = '''
        </table>
'''

FUNC_FOR_SEARCH = '''
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

SEARCH_INPUT = '''
        <h2>My Filter</h2>
        <input type="text" id="myInput" onkeyup="myFunction()" placeholder="Search for names..." title="Type in a name" style="border-color:green;border-width:10px;border-style:ridge;">
'''

