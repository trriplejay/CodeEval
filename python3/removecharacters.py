import sys


if __name__ == '__main__':
    """
    given a string and a set of characters, remove each occurrence of the set
    of characters from the string
    """

    if sys.argv[1]:
        try:
            file = open(sys.argv[1])
        except IOError:
            print('cannot open', sys.argv[1])
        else:
            """
            loop through the file, read a line, strip it, split it by comma
            to get the string and the character sequence, then split the string
            into a list of characters.
            """
            for line in file:
                thestring, thechars = line.strip().split(',')
                # get rid of that 1 extra whitespace
                thechars = thechars.strip()
                # use python list comprehension to do the comparisons
                modifiedStr = [x for x in list(thestring) if x not in thechars]
                print("".join(modifiedStr))

    else:
        print("no input file provided")
