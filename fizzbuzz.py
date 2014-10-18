import sys


def fizzbuzz(x, y, N):
    """
    count from 1 to N, printing each number along the way.
    if current count is divisible by x, print F instead of the number
    if current count is divisible by y, print B instead of the number
    if current count is divisible by both x and y, print FB instead of number
    make sure each print is separated by a " "
    """

    #print("inside fizzbuzz with params:",x, y, N)

    for i in range(1, N+1):
        theStr=""
        if(i % x == 0):
            theStr+="F"
        if(i % y == 0):
            theStr+="B"
        if not theStr:
            theStr+=str(i)

        # the last line shouldn't end in a space
        if i == N:
            print(theStr, end='')
        else:
            print(theStr, end=' ')

    # newline once our work is done
    print()


if __name__ == '__main__':

    # argv[0] is the name of the program, argv[1] will bethe name of
    # the input file
    if sys.argv[1]:
        try:
            file = open(sys.argv[1])
        except IOError:
            print('cannot open', arg)
        else:
            """
            Open the file, and read it line by line.  Each line equates to
            one call of the fizzbuzz function and will result in one line
            of output.  Keep looping until the end of the file is reached
            """

            # loop through the file, read one line at a time, strip it, and
            # split it into a list.  The resulting list should have 3 elements
            for line in file:
                line = line.strip().split(" ")

                # Instructions say that it is safe to assume the file
                # is formatted correctly.
                # Call fizzbuzz, passing in each element from the line as
                # an integer
                fizzbuzz(int(line[0]), int(line[1]), int(line[2]))

    else:
        print("no input file provided")
