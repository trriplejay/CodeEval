import sys


def do_math(a, b, op):
    if op == "+":
        return int(a) + int(b)
    else:
        return int(a) - int(b)


if __name__ == '__main__':
    """
    given a number, and a list of characters with an operator, perform the
    operation on the number after splitting the number at the same location
    as the operator
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
                thenumber, thechars = line.strip().split(' ')
                # find the index and value of the operator
                opindex = thechars.find("+")+thechars.find("-")+1
                theOperator = thechars[opindex]
                # substring the numbers at opindex and perform the operator
                # on them

                result = do_math(
                    thenumber[:opindex:],
                    thenumber[opindex::],
                    theOperator
                )

                print(result)

    else:
        print("no input file provided")
