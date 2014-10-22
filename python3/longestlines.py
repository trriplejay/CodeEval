import sys


if __name__ == '__main__':
    """
    given a number of lines to print (n), and a list of strings, print out
    the longest n strings
    """

    if sys.argv[1]:
        try:
            file = open(sys.argv[1])
        except IOError:
            print('cannot open', sys.argv[1])
        else:
            #first line is the number of lines of output
            lines_to_output = int(file.readline().strip())

            """
            loop through the file, read one line at a time, store it in a
            list of tuples where first element is the string, second is
            the length of the string
            """
            strTuple = []
            for line in file:
                # do some list comprehension, only keep the alphabetical items
                strTuple.append((line.strip(), len(line)))
                # pull out a list of unique letters

            final = sorted(strTuple, key=lambda srt: srt[1], reverse=True)
            for i in range(0, lines_to_output):
                print(final[i][0])

    else:
        print("no input file provided")
