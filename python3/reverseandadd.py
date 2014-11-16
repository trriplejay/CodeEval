import sys

"""
reverse and add:
  take a number as input, reverse it, and add it to its original value
  repeat the process until the result is a pallindrome.  The description
  guarantees that this will happen in 100 iterations or less for any
  given input number.
"""


def find_pall(num_str):
    """ returns the pallindrome or None if iterations exceed 150
    """
    count = 0

    while(num_str != num_str[::-1] and count < 150):
        num_str = str(int(num_str) + int(num_str[::-1]))
        count += 1
    return str(count), num_str



if __name__ == '__main__':

    # assume input was correctly given, no need to error check

    thefile = open(sys.argv[1])
    numlist = list()
    for line in thefile:
        # lets use list comprehension to run all inputs at once, rather
        # than one line at a time
        num = line.strip()
        # append all elements to a list
        numlist.append(num)

    # use map to perform find_pall on each item. print the results
    for item in map(find_pall, numlist):
        # unpack the tuple
        count, pall = item
        print(count + " " + pall)
