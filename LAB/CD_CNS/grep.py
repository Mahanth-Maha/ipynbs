import re
import sys
import glob

if len(sys.argv) < 2 :
    print('USAGE : python grep.py [OPTION...] PATTERNS [FILE...]')
if '--help' in sys.argv : 
    print(''' GREP(1)                       User Commands                      GREP(1)
NAME
       python grep.py - print lines that match patterns
SYNOPSIS
       python grep.py [OPTION...] PATTERNS [FILE...]
DESCRIPTION
       grep.py searches for PATTERNS in each FILE.  PATTERNS is one or more
       patterns separated by newline characters, and grep prints each
       line that matches a pattern.  Typically PATTERNS should be quoted
       when grep is used in a shell command.
OPTIONS
   Generic Program Information
       --help Output a usage message and exit. ''')

for arg in sys.argv[2:]:
    print("Search Results from file : ",arg)
    for file in glob.iglob(arg):
        for line in open(file, 'r'):
            if re.search(sys.argv[1], line):
                print(line.replace('\n','')) 