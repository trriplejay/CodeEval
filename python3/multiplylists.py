import sys

if __name__ == '__main__':
    """
    Take input in the form of two lists of numbers.
    multiply the corresponding indecies of numbers and output the
    resulting list
    """

    if sys.argv[1]:
        try:
            file = open(sys.argv[1])
        except IOError:
            print('cannot open', sys.argv[1])
        else:

            """
            loop through the file, read one line at a time, strip it, then
            split it into a list, sum the items, and print it out
            """
            for line in file:
                # separate the lists based on teh '|' character
                lists = line.strip().split("|")
                # split each individual list on whitespace
                list_one = lists[0].strip().split(" ")
                list_two = lists[1].strip().split(" ")
                # initialize the list that will store the results
                results = []

                for i in range(0, len(list_one)):
                    # perform the multiplication and add the result to the list
                    results.append((str(int(list_one[i])*int(list_two[i]))))

                # join the list with whitespace and print it
                print(" ".join(results))

    else:
        print("no input file provided")
