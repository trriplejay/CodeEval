import sys

if __name__ == '__main__':

    if sys.argv[1]:
        try:
            file = open(sys.argv[1])
        except IOError:
            print('cannot open', arg)
        else:

            """
            loop through the file, read one line at a time, strip it, then
            split it into a list, reverse it, paste it back together and
            print it out! no extra function definition needed
            """
            for line in file:
                line = line.strip().split(" ")
                # ignore empty lines
                if line[0] != '':
                    print(" ".join(reversed(line)))

    else:
        print("no input file provided")