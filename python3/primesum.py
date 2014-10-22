

def is_prime(n):
    """
    test if a number is prime, return a bool
    """

    if ((n == 2)or(n == 3)):
        # get these common primes out of the way, since our formula
        # later on would get bad results from these
        return True
    # just in case someone tries to test an even number, or the number 1
    if (n % 2 == 0) or (n == 1):
        return False

    # to test for a prime, one way to do it is to attempt to mod the number
    # with evertying odd number great than or equal to 3, up to the square
    # root of n
    for i in range(3, int(n**.5)+2):
        if n % i == 0:
            return False

    # if we make it this far, the primality test is passed
    return True


def sum_primes(n):
    """
    returns the sum of the first n primes (don't make n too big now!)
    """
    # start at 2, since 1 is not considered prime
    current_num = 2
    final_sum = 0
    count = 1
    while count <= n:

        # test for primality.  if it passes, add the prime to the sum
        # and increment our counter
        if is_prime(current_num):
            final_sum += current_num
            count += 1

        current_num += 1
    return final_sum

if __name__ == '__main__':

    #challenge asks for the sum of the first 1000 prime numbers
    print(sum_primes(1000))
