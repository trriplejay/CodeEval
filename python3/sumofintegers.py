import sys

"""Sum of integers:
    find the largest sum of a continuous subseries of numbers given an input
    list. print the sum
"""


if __name__ == '__main__':

    thefile = open(sys.argv[1])

    for line in thefile:

        # split on the comma
        line = line.strip().split(',')

        # convert input into integers so we can do math.  This should also
        # eliminate any extra white space for each element
        line = list(map(int, line))

        # keep track of the best result (highest sum)
        best_result = None
        # i will be the end index for our substring
        for i in range(1, len(line) + 1):
            # j will be the starting point for our substring
            for j in range(i-1, -1, -1):
                # sum from start to end of substring
                result = sum(line[j:i:1])
                if best_result is None:
                    best_result = result
                elif result > best_result:
                    best_result = result

        print(best_result)
