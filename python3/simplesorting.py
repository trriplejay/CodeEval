import sys


if __name__ == '__main__':
    """
    given a list of float values, sort them and print them in sorted order
    """

    if sys.argv[1]:
        try:
            file = open(sys.argv[1])
        except IOError:
            print('cannot open', sys.argv[1])
        else:
            """
            loop through the file, read a line, strip it, split it by space,
            convert each item to a float so that the list can be sorted,
            convert each item back to a string so that then can be joined
            and printed as a single string
            """
            for line in file:
                print(
                    " ".join( # space between each number
                        ['{:0.3f}'.format(x) for x in # back to formatted str
                            sorted( # sort the floats
                                map(  # convert to floats
                                    float, line.strip().split(" ") #strip n split
                                )
                            )
                        ]
                    )
                )

    else:
        print("no input file provided")
