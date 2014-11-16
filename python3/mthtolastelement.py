import sys

"""Mth to last element:
    each line of input is a list of letters, followed by a single number
    the number represents the index from the END of the list that we wish
    to print out.  Ignore if the index is larger than the list itself
"""

if __name__ == '__main__':

    thefile = open(sys.argv[1])

    for line in thefile:
        # split the line on whitespace
        line = line.strip().split(" ")
        # POP the last element.  it is the index.
        index = int(line.pop())
        # check that index isnt bigger than total list
        if index <= len(line):
            # print the index we're looking for
            print(line[-index])
