"""
ps.py
Launches Library/Frameworks/Python.framework/Versions/3.6/bin/pip3 list --format=legacy"
see what files are running
put them in a list
print list 
"""

import sys
import os

infile = os.popen("/Library/Frameworks/Python.framework/Versions/3.6/bin/pip3 list --format=legacy")   #Create a child process and a pipe.

lines = infile.readlines()          
status = infile.close()

if status != None:                   
    print("\"pip3 list --format=legacy\" produced exit status", status)
    sys.exit(1)

lines = set(lines[1:])                          
for i, line in enumerate(lines, start = 1):
    print("{} {}".format(i, line))

sys.exit(0)
