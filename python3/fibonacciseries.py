import sys


class memoize():
    """
    Decorate a function with this.
    To memoize something, we use the arguments to the original function as
    a key in a dict.  The value associated with that key will be the result
    of calling the memoized function with those same arguments.  If the
    result has already been calculated, we can just return it from our dict
    otherwise, call the original function, store the result in the dict,
    then return the result.
    """

    def __init__(self, func):

        self.dict = {}
        self.func = func

    def __call__(self, *args):
        #check our dict for the presence of args
        if args in self.dict:
            return self.dict[args]
        else:
            result = self.func(*args)
            self.dict[args] = result
            return result


@memoize
def fib(n):
    """
    calculate the nth fibonacci number
    via recursion
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


if __name__ == '__main__':

    if sys.argv[1]:
        try:
            file = open(sys.argv[1])
        except IOError:
            print('cannot open', sys.argv[1])
        else:

            """
            loop through the file, read one line at a time, strip it, then
            call funtion to calculate result
            """
            for line in file:
                #only one number per line, so just strip the line
                num = int(line.strip())
                print(fib(num))

    else:
        print("no input file provided")