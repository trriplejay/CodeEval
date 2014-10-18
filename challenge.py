import sys


if __name__ == '__main__':
    """
    given a list of strings, determine the maximum possible value of each
    string, when letters take on a value between 1 and 26, and no two letters
    have the same value.
    """

    if sys.argv[1]:
        try:
            file = open(sys.argv[1])
        except IOError:
            print('cannot open', sys.argv[1])
        else:
            """
            loop through the file, read one line at a time, strip it, make
            it lowercase since case does not matter for this exercise.
            """
            for line in file:
                # do some list comprehension, only keep the alphabetical items
                letters = [x for x in list(line.strip().lower()) if x.isalpha()]
                # pull out a list of unique letters
                uniqueletters = set(letters)

                # start with the highest value a letter can have
                value = 26
                # beauty starts at 0
                beauty = 0
                # a list of tuples, a letter and how often it occurs
                countuple = []
                for letter in uniqueletters:
                    # add a unique letter to the list of tuples along with
                    # how many times it occurs in the original string
                    countuple.append((letter, letters.count(letter)))

                # sort based on the letter count, with high frequencies in
                # the front of the list
                countuple = sorted(countuple, key=lambda srt: srt[1], reverse=True)

                # highest frequency letters take on the highest value, every
                # subsequent letter has it's value lowered by 1
                for letter, howmany in countuple:
                    # since we know how often a letter occurs, we can multiply
                    beauty += value * howmany
                    value -= 1


                print(beauty)

    else:
        print("no input file provided")
