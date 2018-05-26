
import sys
import re

infile = sys.argv[1]
fd = open(infile, 'r')

while True:
    line = fd.readline()
    if len(line) == 0:
        break

    #m = re.match('((\w+\s*/*\d*\.*)\t*)+', line)
    m = re.match('(.*?)\t+(.*?)\t+(.*?)\t+(.*?)\t+(.*)$', line)
    if not m:
        continue
    print("%s,%s" % (m.group(1), m.group(4)))
