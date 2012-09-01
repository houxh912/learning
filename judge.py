#!/usr/bin/python

import sys


if len(sys.argv) != 3:
	print "set the para default"
	file1_name = 'a.txt'
	file2_name = 'b.txt'
else:
	file1_name = sys.argv[1]
	file2_name = sys.argv[2]

f1 = file(file1_name,'r')
f2 = file(file2_name,'r')

while True:
	line1 = f1.readline()
	line2 = f2.readline()
	if(len(line1) != len(line2)):
		print "not equ:"
		print line1,
		print line2,
		break
	elif (len(line1) == 0 and len(line2) == 0):
		print "equ";
		break
	elif (len(line1) == 0 or len(line2) == 0):
		print "not equ:"
		print line1,
		print line2,
		break
f1.close()
f2.close()

