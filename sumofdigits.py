import sys

if __name__ == '__main__':

    if sys.argv[1]:
        try:
            file = open(sys.argv[1])
        except IOError:
            print('cannot open', sys.argv[1])
        else:

            """
            loop through the file, read one line at a time, strip it, then
            split it into a list, sum the items, and print it out
            """
            for line in file:
                # use 'sum' function to reduce the list down to a single
                # digit that is the sum of all items in the list
                # but first, use the map function to convert the list
                # of strings into a list of integers, so that they can
                # be summed
                print(sum(map(int, list(line.strip()))))



    else:
        print("no input file provided")