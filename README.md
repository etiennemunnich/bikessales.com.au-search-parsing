# bikessales.com.au-search-parsing

This was a quick experiment working to gather some data for pricing on motorcycles from bikesales.com.au whilst learning how to using BS4.

Note: Line 33 can be editted such that filters from the website are used, such as year make model etc. 

Requirements
 - Python3.7+
 - Beautiful Soup 4
 - Requests
 
Install modules:
  > pip3 install bs4 requests argparse
  
Usage:
  > python main.py -h

   usage: main.py [-h] [-v] [-p PAGES] [--version]

   optional arguments:
     -h, --help            show this help message and exit
     -v, --verbose         Verbosity (-v, -vv, etc)
     -p PAGES, --pages PAGES
                           12 items a page, choose the number of pages.
     --version             show program's version number and exit
     
