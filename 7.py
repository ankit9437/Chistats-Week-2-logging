#7. WAF to find factorial of given number

import logging
def fact(a):
    if(a==1):
        return (1)
    else:
        return ((a*fact(a-1)))

a=int(input())
logging.basicConfig(filename= '6test.log',level=logging.DEBUG, format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
logging.debug(fact(a))

"""Output
4
20-May-21 15:25:50 - 24"""