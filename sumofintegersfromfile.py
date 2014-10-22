import sys

if __name__ == '__main__':
    """
    Each line contains one integer.  Read each line, and add each integer to
    the total. print out the total
    """
    if sys.argv[1]:
        try:
            file = open(sys.argv[1])
        except IOError:
            print('cannot open', sys.argv[1])
        else:

            """
            loop through the file, read one line at a time, strip it, cast it
            to an int, and add the result to the total
            """
            theSum = 0
            for line in file:
                # use 'sum' function to reduce the list down to a single
                # digit that is the sum of all items in the list
                # but first, use the map function to convert the list
                # of strings into a list of integers, so that they can
                # be summed
                theSum += int(line.strip())

            print(theSum)

    else:
        print("no input file provided")