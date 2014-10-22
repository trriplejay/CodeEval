import sys
#import string


if __name__ == '__main__':
    """
    Determine if a number is "happy" by taking the sum of the square of its
    digits until the result hits value 1, or until you detect a loop that does
    not include the value 1.  Output 1 for numbers that reach 1, and 0 for
    numbers that do not.
    """

    if sys.argv[1]:
        try:
            file = open(sys.argv[1])
        except IOError:
            print('cannot open', sys.argv[1])
        else:
            """
            loop through the file, read one line at a time, strip it
            """
            for line in file:
                number = line.strip()
                numlist = []
                # get the first number ready
                theNext = number
                while theNext != 1:
                    # break the number into individual digits
                    digits = map(int, list(str(theNext)))
                    # sum the squares of the digits
                    theNext = sum([x**2 for x in digits])
                    # check for cycle
                    if theNext in numlist:
                        # if the number already exists, we must be in a loop
                        # print 0 and break from loop
                        print("0")
                        break
                    else:
                        # append the number to a list to watch for cycles
                        numlist.append(theNext)
                if theNext == 1:
                    print("1")

    else:
        print("no input file provided")
