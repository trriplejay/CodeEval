import sys

if __name__ == '__main__':

    if sys.argv[1]:
        try:
            file = open(sys.argv[1])
        except IOError:
            print('cannot open', sys.argv[1])
        else:

            """
            loop through the file, read one line at a time, turn it into a
            python list, then call upper or lower on alternating characters.
            Use a boolean toggle to do so.  If the character is non-alpha,
            don't toggle, but still add it to the output string.
            """
            for line in file:
                toggle = True
                finalline = ""

                # calling list turns the string into a list of characters
                for letter in list(line.strip()):
                    if letter.isalpha():
                        if toggle:
                            finalline += letter.upper()
                            toggle = False
                        else:
                            finalline += letter.lower()
                            toggle = True

                    else:
                        # don't toggle if its not an alphabetical character
                        finalline += letter
                print(finalline)

    else:
        print("no input file provided")
