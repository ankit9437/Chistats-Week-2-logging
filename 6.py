#6. WAF which takes two number as parameter, calculates the sum of square of the parameters and returns it

import logging
def sq(a,b):
    logging.debug((a*a)+(b*b))

a=int(input())
b=int(input())
logging.basicConfig(filename= '6test.log',level=logging.DEBUG, format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
logging.info('Admin logged in')
sq(a,b)

"""Output
20-May-21 15:23:03 - Admin logged in
20-May-21 15:23:03 - 20"""