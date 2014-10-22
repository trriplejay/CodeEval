import sys


def is_op(n):
    """
    returns true if the given input is within the allowed
    operators of this challenge
    """
    if n == '/' or n == '+' or n == '*':
        return True


def calc_result(op, num1, num2):
    """
    translates the operators character into its action
    and takes that action on the provided input
    """
    if op == '/':
        return num1 / num2
    elif op == '+':
        return num1 + num2
    elif op == '*':
        return num1 * num2


if __name__ == '__main__':
    """
    calculate a provided prefix expression.  We are assuming the provided
    expression is valid
    """

    if sys.argv[1]:
        try:
            file = open(sys.argv[1])
        except IOError:
            print('cannot open', sys.argv[1])
        else:
            """
            loop through the file, read a line, strip it, split it by space.
            """
            for line in file:
                items = list(line.strip().split())
                theStack = []

                for item in items:
                    if is_op(item):
                        # next item is an operator, push it on the stack
                        theStack.append(item)
                    else:
                        # item not an operator
                        if is_op(theStack[-1]):
                            # no number on the stack, push this one
                            theStack.append(item)
                        else:
                            # top of the stack is a number, and we're
                            # attempting to push another, so pop the top
                            # number and the operator and perform the calc
                            # may need to perform multiple calcs if the
                            # resulting stack still has a number on top
                            num2 = float(item)
                            while theStack and not is_op(theStack[-1]):

                                num1 = float(theStack.pop())
                                op = theStack.pop()
                                # don't push yet, see if there is more to
                                # calculate in additional iterations
                                num2 = calc_result(op, num1, num2)
                            #push the result back onto the stack
                            theStack.append(num2)
                if theStack:
                    print(int(theStack.pop()))

    else:
        print("no input file provided")
