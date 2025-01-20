#!/usr/bin/env python3 

import sys

title = sys.argv[0]
if len(sys.argv) != 3:
    print('Usage: ' + title + ' name age')
    sys.exit(0)
name = sys.argv[1]
age = sys.argv[2]
print('Hi ' + name + ', you are ' + age + ' years old.')




#print('Hi ' + name + ', you are ' + str(age) + ' years old.')
