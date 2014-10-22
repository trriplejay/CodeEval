import sys


def rec_pref(items):
    # use recursion to calculate the results.
    item = items.pop(0)

    if item == '+':
        return rec_pref(items) + rec_pref(items)
    if item == '/':
        return rec_pref(items) / rec_pref(items)
    if item == '*':
        return rec_pref(items) * rec_pref(items)
    else:
        return float(item)


if __name__ == '__main__':
    """
    calculate a provided prefix expression.  We are assuming the provided
    expression is valid.  I tried a stack implementation but didn't get full
    points... not sure what scenario I was missing, but I figured I'd do a
    recursive version and see if this holds up better.
    """

    if sys.argv[1]:
        try:
            file = open(sys.argv[1])
        except IOError:
            print('cannot open', sys.argv[1])
        else:
            """
            loop through the file, read a line, strip it, split it by space.
            """
            for line in file:
                items = list(line.strip().split())
                if items:
                    print(int(rec_pref(items)))

    else:
        print("no input file provided")
