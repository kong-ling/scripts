import re
import os
import sys
import string
import datetime

currentDir = os.getcwd()
currentTime = datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
print(currentDir, '\n', currentTime)

TABLE = '''
<input type="text" id="myInput" onkeyup="myFunction()" placeholder="Search for names..">

<table id="myTable">
  <tr class="header">
    <th style="width:60%;">Name</th>
    <th style="width:40%;">Country</th>
  </tr>
  <tr>
    <td>Alfreds Futterkiste</td>
    <td>Germany</td>
  </tr>
  <tr>
    <td>Berglunds snabbkop</td>
    <td>Sweden</td>
  </tr>
  <tr>
    <td>Island Trading</td>
    <td>UK</td>
  </tr>
  <tr>
    <td>Koniglich Essen</td>
    <td>Germany</td>
  </tr>
</table>
'''

TABLE_ESSENCE = '''
<input type="text" id="myInput" onkeyup="myFunction()" placeholder="Search for names..">

<table id="myTable" border=1px>
  <tr class="header">
    <th style="width:60%;">Name</th>
  </tr>
  <tr>
    <td>Alfreds Futterkiste</td>
  </tr>
</table>
'''

TABLE_ESSENCE_head = '''
<input type="text" id="myInput" onkeyup="myFunction()" placeholder="Search for names..">

<table id="myTable">
  <tr class="header">
    <th style="width:60%;">Name</th>
  </tr>
'''

FILTER = '''
</table>
<script>
function myFunction() {
  // Declare variable
  var input, filter, table, tr, td, i, txtValue;
  input = document.getElementById("myInput");
  filter = input.value.toUpperCase();
  table = document.getElementById("myTable");
  tr = table.getElementsByTagName("tr");

  // Loop through all table rows, and hide those who don't match the search query
  for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[0];
    if (td) {
      txtValue = td.textContent || td.innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }
  }
}
</script>
'''

HEADER = '''
<nav data-toggle="wy-nav-shift" class="wy-nav-side">
    <div class="wy-side-scroll">

        <div class="wy-menu wy-menu-vertical" data-spy="affix" role="navigation" aria-label="main navigation" style="color:green;font-size:120%">
            <ul>
'''

FOOTER = '''
            </ul>
        </div> <!-- wy-menu wy-menu-vertical -->
    </div>     <!-- wy-side-scroll -->
</nav>
'''



#html_file = open('index_new.html', 'w')
html_file = open(sys.argv[1], 'w')

html_file.write(TABLE_ESSENCE_head)

TABLE_ESSENCE_line1 = '''
  <tr>
    <td>
'''

TABLE_ESSENCE_line2 = '''
    </td>
  </tr>
'''

TABLE_ESSENCE_line3 = '''
  <tr>
    <td>%s</td>
  </tr>
'''
#for root, dirs, files in os.walk(currentDir):
for root, dirs, files in os.walk('.'):
    for file in files:
        (filepath, file_ext) = os.path.splitext(file)
        #if os.path.splitext(file)[1] == '.html':
        if file_ext == '.html':
            print(root + '/' + file)
            #print(root + ',' + file)
            #line = '                <li class="toctree-l1"><a class="reference internal" href="%s/%s">%s</a></li>' % (root, file, file)
            line = '                <li class="toctree-l1"><a  href="%s/%s">%s</a></li>' % (root, file, filepath)
            html_file.write('%s %s %s' % (TABLE_ESSENCE_line1, line, TABLE_ESSENCE_line2))

html_file.write(FILTER)
html_file.write(FOOTER)
html_file.close()
