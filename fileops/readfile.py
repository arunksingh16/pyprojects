# reading a file

import os
import sys

f = open(sys.argv[1], mode='rt', encoding='utf-8')
for line in f:
  #print(line)
  # instead of print use sys.stdout.write() // it will help you in removing trailing new line characters added by print
  sys.stdout.write(line)
f.close()


# python readfile.py file.txt
