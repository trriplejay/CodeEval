import sys
#import string


if __name__ == '__main__':
    """
    Given a sorted list of numbers, extract the unique numbers and print them
    This is made trivial by the python "set" structure.  Unique elements can be
    extracted from a list simply by assigning the list to a new set.
    However, I'll avoid using that for this exercise.
    """

    if sys.argv[1]:
        try:
            file = open(sys.argv[1])
        except IOError:
            print('cannot open', sys.argv[1])
        else:
            """
            loop through the file, read one line at a time, strip it, split it,
            check for unique numbers, print them
            """
            for line in file:
                numbers = line.strip().split(",")
                unique_numbers = []
                # set our first number as a point of comparison
                unique_numbers.append(numbers[0])
                unique_index = 0
                for i in range(0, len(numbers)):
                    # we know the numbers are sorted, so we can just
                    # keep comparing until we find one that doesn't match
                    if unique_numbers[unique_index] == numbers[i]:
                        pass
                    else:
                        unique_numbers.append(numbers[i])
                        unique_index += 1

                # rejoin the numbers to form the original string
                print(",".join(unique_numbers))


                # the real python3 implementation would just need to
                # instantiate a set, passing the list of numbers in as
                # a parameter:
                # print(",".join(sorted(set(numbers))))
    else:
        print("no input file provided")
