# Egyptian fractions

import math

def egyptian_frac(numerator, denominator):
    # creating our list of denominators for our Egyptian fractions
    egypt_list = []
    while numerator != 0:

        x =math.ceil(denominator/numerator)
        egypt_list.append(x)

        numerator = x * numerator - denominator
        denominator *= x

    str = ''

    for ones in egypt_list:
        str += '1/{0} + '.format(ones)
    final_string = str[:-3]

    return final_string

print(egyptian_frac(7, 12))