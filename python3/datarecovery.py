import sys


def recover_data(words, ordering):
    """
    takes in a list of words, and a list of integers, and rearranges
    the words based on the ordering of the integers, then returns
    the rearranged list of words
    """

    # first, build a dict with the words/values.  There seems to always be
    # one word at the end that does not have a corresponding number.  This
    # is probably because you still have enough information to reconstruct
    # the sentence without that extra number.
    mydict = {}

    for i in range(0, len(ordering)):
        mydict[ordering[i]] = words[i]

    # next, sort the list of numbers
    ordering.sort()

    #now, build a new list in order of the sorted numbers
    finalwords = []

    for i in range(1, len(words)+1):
        if i in mydict:
            finalwords.append(mydict[i])
        # this was the word that did not have a number associated with
        # it.  It is always last in the input, and will simply fill
        # whatever slot is missing a word when reconstructing the sentence
        else:
            finalwords.append(words[-1])
    return finalwords


if __name__ == '__main__':

    if sys.argv[1]:
        try:
            file = open(sys.argv[1])
        except IOError:
            print('cannot open', sys.argv[1])
        else:

            """
            loop through the file, read one line at a time, strip it, then
            split 3 times, creating 2 lists.  first split is on ';' to
            separate the words from the ordering.  Second split is on the [0]
            index of the first split, to make a list out of the words.  The
            third split is a split of the [1] index from the original split.
            This will split the ordering into a list of integers
            """
            for line in file:
                first_split = line.strip().split(";")
                words = first_split[0].split(" ")
                numbers = list(map(int, first_split[1].split(" ")))
                print(" ".join(recover_data(words, numbers)))

    else:
        print("no input file provided")
