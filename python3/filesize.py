import os
import sys
"""
very simple in python.  assume correct inputs
"""

filesize = os.path.getsize(sys.argv[1])
print(filesize)
