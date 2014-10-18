def lower_prime_pal(n):
    """
    Finds the highest prime pallindrome that is lower than the given input "n"
    """

    # if n is 3 or less, it's already the lowest prime it can be
    if n <= 3:
        return n
    #change the value n to be the next lowest odd number from the given n
    #this will subtract 1 if the number given was even, and 2 if it was odd
    n -= 1 + n%2

    while 1:
        """
        As a general rule, you can test for the primality of 'n' by
        attempting to divide it by all odd numbers from 3 to the square
        root of n.  This implementation uses python list comprehension to
        create an array of true/false values, which then are logically OR'd
        together by the 'any' function.  If even one of the mod x operations
        resulted in 0, the number is not prime.
        """

        # First test for pallindrome, since that's more time efficient
        # than testing for primality.
        # Here's a pythonic test for a pallindrome.
        if str(n)==str(n)[::-1]:
            #the number is a pallindrome, but is it prime?
            if not any([n%x==0 for x in range(3,int(n**.5)+2)]):
                # success, return the number
                return n
        # decrement our number, as we're counting down to find the
        # next highest
        n-=2


if __name__ == '__main__':

    #challenge asks for the next prime pallindrome lower than 1000
    print (lower_prime_pal(1000))
