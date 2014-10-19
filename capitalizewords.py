import sys
#import string


if __name__ == '__main__':
    """
    Given a string, capitalize each word in the string and print it out.
    This exercise becomes a bit trivial with the built-in capwords helper
    function in python 3, so i'll do it manually instead using .upper()
    by splitting each word into letters, capitalizing first letter, and
    rejoining the string to print
    """

    if sys.argv[1]:
        try:
            file = open(sys.argv[1])
        except IOError:
            print('cannot open', sys.argv[1])
        else:
            """
            loop through the file, read one line at a time, strip it, split it,
            capitalize one word at a time, rejoin the words, and print it out
            """
            for line in file:
                words = line.strip().split(" ")
                for i in range(0, len(words)):
                    # turn the word into a list of letters
                    letters = list(words[i])
                    # capitalize the first letter
                    letters[0] = letters[0].upper()
                    # rejoin the letters to form a word
                    words[i] = "".join(letters)
                # rejoin the words to form the original string
                print(" ".join(words))


                # the real python3 implementation would just need to call
                # a single helper function:
                #print(string.capwords(line))
    else:
        print("no input file provided")
