import sys


class mystack():

    def __init__(self):
        """
        still going to use a python list
        """
        self.numbers = []
        self.count = 0

    def push(self, n):
        """
        push n onto the stack by using built-in "append" function
        add to the count. (no real reason to keep track manually)
        """
        self.numbers.append(n)
        self.count += 1

    def pop(self):
        """
        Pop the most recently pushed number off the stack and return it
        This will be the last item in the list (FIFO).
        If the list is empty, just return false, to avoid raising a "pop
        from empty list" error
        """
        if self.count > 0:
            #instantly access the last number in the list
            self.count -= 1
            return self.numbers.pop()
        else:
            return False


if __name__ == '__main__':
    """
    Seems like cheating to do this in python... I may implement later in C.
    I decided to build a class to act as an interface to a python "stack"
    even though the problem could be solved with the build in functionality
    of a python list.
    Lets say that I don't want to show an error if i try to pop an empty stack.
    I only want to return false instead.  My class will wrap around a built-in
    list to allow that functionality
    """

    if sys.argv[1]:
        try:
            file = open(sys.argv[1])
        except IOError:
            print('cannot open', sys.argv[1])
        else:

            """
            loop through the file, read one line at a time, strip it, then
            split it into a list.  Instantiate a "mystack" object, push
            each value onto the stack, then pop every value, printing only
            every other value
            """
            for line in file:
                line = line.strip().split(" ")
                theStack = mystack()

                # push the items
                for num in line:
                    theStack.push(int(num))

                # pop them all and print every other
                while theStack.count > 0:
                    print(theStack.pop(), end=' ')
                    theStack.pop()

                print()

    else:
        print("no input file provided")
