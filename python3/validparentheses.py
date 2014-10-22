import sys


def is_open(paren):
    """
    returns true if the passed in value is an open paren, or brace, or bracket
    """
    return (paren == '(' or paren == '[' or paren == '{')


def match_paren(a, b):
    """
    returns true if a and b are open and closed parentheses of the same type
    """
    if a == '[':
        return b == ']'
    elif a == '(':
        return b == ')'
    elif a == '{':
        return b == '}'


if __name__ == '__main__':
    """
    given an input string of open/close parentheses, determine if they are
    properly matched.
    """

    if sys.argv[1]:
        try:
            file = open(sys.argv[1])
        except IOError:
            print('cannot open', sys.argv[1])
        else:
            """
            loop through the file, read one line at a time, strip it, then
            split it into a list.
            """
            for line in file:
                line = list(line.strip())
                result = True
                pStack = []
                for paren in line:
                    # if it's an open paren, push it onto pStack
                    if is_open(paren):
                        pStack.append(paren)
                    else:
                        # check the top value. if the list is empty, it mean
                        # that all parens have matched so far, but if we're
                        # inside this else, it means we're trying to add
                        # a close paren, so it must be unmatched, and we can
                        # break with a False return
                        if not pStack:
                            result = False
                            break
                        stacktop = pStack[-1]
                        if match_paren(stacktop, paren):
                            #they match properly, pop the top
                            pStack.pop()
                        else:
                            #this is  not a valid string. set result
                            #and stop looping
                            result = False
                            break
                if pStack:
                    # if there is one item left in the list after iterating
                    # make sure to fail, since it is unmatched
                    result = False
                print(str(result))
    else:
        print("no input file provided")
