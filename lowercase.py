import sys


if __name__ == '__main__':
    """
    loop through the input file, calling "lower()" on each line.  quite
    simple in python
    """

    if sys.argv[1]:
        try:
            file = open(sys.argv[1])
        except IOError:
            print('cannot open', sys.argv[1])
        else:

            """
            loop through the file, read one line at a time, call "lower()" on
            it and print it out.

            """
            for line in file:
                print(line.lower(), end='')

    else:
        print("no input file provided")