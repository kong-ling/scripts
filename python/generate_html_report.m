function generate_html_report
   
   testlist = sprintf('%s/testlist.txt', getenv('workAlgorithms'));
   %enter Rootdir
   root_dir = lteGetTestRootDir('', 'hw');
   chdir(root_dir);
   %generate html report 
   run_python_file = sprintf('python %s/lteTest/functions/testUtil/generate_html.py %s', getenv('workAlgorithms'), testlist);
   fprintf('%s\n', run_python_file);
   
   %run python file with parameter
   system(run_python_file);
