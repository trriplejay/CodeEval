import sys


if __name__ == '__main__':
    """
    given a value to reach, output the minimum number of coins needed to reach
    the value assuming coins have values of 1, 3, and 5
    """

    if sys.argv[1]:
        try:
            file = open(sys.argv[1])
        except IOError:
            print('cannot open', sys.argv[1])
        else:
            """
            loop through the file, read one line at a time, strip it, convert
            it to an int.  It is the value we are trying to reach
            """
            for line in file:
                value = int(line.strip())
                fives = value // 5
                remain = value % 5
                threes = remain // 3
                remain = remain % 3
                totalcoins = fives + threes + remain

                print(totalcoins)
    else:
        print("no input file provided")
