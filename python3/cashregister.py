import sys
from collections import OrderedDict
from decimal import Decimal

"""Cash register:
    given a price and an amount of cash given by a customer, calculate their
    change and return it as a string of keys from a dictionary
"""


def get_change(pp, ch):

    # Floating point math can get tricky at the 0.0x decimal level,
    # leading to inaccurate results, so I'm opting to use the python
    # "Decimal" library for all math

    change_needed = ch - pp

    if change_needed < 0:
        return ["ERROR"]
    elif change_needed == 0:
        return ["ZERO"]
    else:
        # initialize empty result list
        result = list()
        # ordered dict maintains the order in which we insert items,
        # so when we iterate over it, we can iterate in the same order
        moneydict = OrderedDict([
            ('ONE HUNDRED', Decimal('100.00')),
            ('FIFTY', Decimal('50.00')),
            ('TWENTY', Decimal('20.00')),
            ('TEN', Decimal('10.00')),
            ('FIVE', Decimal('5.00')),
            ('TWO', Decimal('2.00')),
            ('ONE', Decimal('1.00')),
            ('HALF DOLLAR', Decimal('.50')),
            ('QUARTER', Decimal('.25')),
            ('DIME', Decimal('.10')),
            ('NICKEL', Decimal('.05')),
            ('PENNY', Decimal('.01'))
        ])
        for key, value in moneydict.items():
            while change_needed.compare(value) >= 0:
                result.append(key)
                change_needed = change_needed - value

        return result


if __name__ == '__main__':

    thefile = open(sys.argv[1])

    for line in thefile:
        # split up the cost, and the cash given
        pp, ch = list(map(Decimal, line.strip().split(";")))

        # call the function to do all the work
        result = get_change(pp, ch)
        # join the results
        print(",".join(result))
