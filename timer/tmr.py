#!/usr/bin/env python

# A simple script to notify that you're using the computer for too long

# This works, but use bash version instead. No need for python

from PIL import Image
import time
import sys

assert len(sys.argv) == 2, "Wrong number of arguments"

number_of_sec = int(sys.argv[1])

for _ in range(number_of_sec):
    time.sleep(1)

img = Image.open('/usr/bin/relax.jpg')
img.show()