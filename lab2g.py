#!/usr/bin/env python3 

import sys

# Author: Ademola Noah
# Author ID: 129556221
# Date Created: 2025/01/20

if len(sys.argv) > 1:
    timer = int(sys.argv[1])
else:
    timer = 3

while timer >0:
    print (timer)
    timer = timer - 1
print ('blast off!')
