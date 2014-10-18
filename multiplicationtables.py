
def print_tables(n):
    """
    Function that prints the multiplication tables from 1 to n.
    This function will only pad for up to 4 total spaces, so
    if your table contains a 4 digit result, its not going to look
    good.
    """
    for i in range (1, n + 1):
        for j in range (1, n + 1):
            print("%4d" % (i*j), end='')

        print()


if __name__ == '__main__':
    """
    Print out the multiplication table for numbers 1-12.
    All numbers should be padded to take up a total of 4 characters
    """

    print_tables(12)
