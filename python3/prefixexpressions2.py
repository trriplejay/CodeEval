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
        return num1 // num2
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
                # operate from right to left, so just reverse the list
                # and treat as normal
                items = reversed(items)
                theStack = []

                for item in items:
                    if not is_op(item):
                        # if it's a number, add it to the stack
                        theStack.append(item)
                    else:
                        # it's an operator, so we must have at least
                        # 2 numbers on the stack. pop the most recent two
                        # perform the calculation, and push the result
                        # back onto the stack
                        num1 = int(theStack.pop())
                        num2 = int(theStack.pop())
                        theStack.append(calc_result(item, num1, num2))

                print(theStack.pop())

    else:
        print("no input file provided")
