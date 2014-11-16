import sys
import itertools


if __name__ == '__main__':
    """
    given a string, print out all possible permutations of that string,
    separated by commas
    """

    if sys.argv[1]:
        try:
            file = open(sys.argv[1])
        except IOError:
            print('cannot open', sys.argv[1])
        else:
            """
            Python has a built-in function for this in the itertools library
            """
            for line in file:
                thechars = line.strip()
                permlist = []
                for item in itertools.permutations(thechars):
                    permlist.append("".join(item))
                print(",".join(sorted(permlist)))

    else:
        print("no input file provided")
