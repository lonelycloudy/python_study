#this is the first comment
import os
#filename = os.environ.get('PYTHONSTARTUP')
filename = "test.py"
if filename and os.path.isfile(filename):
    execfile(filename)