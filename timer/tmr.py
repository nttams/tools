#!/usr/bin/env python

from PIL import Image
import time
import sys

assert len(sys.argv) == 2, "Wrong number of arguments"

number_of_sec = int(sys.argv[1])

for _ in range(number_of_sec):
    time.sleep(1)

img = Image.open('/usr/bin/relax.jpg')
img.show()