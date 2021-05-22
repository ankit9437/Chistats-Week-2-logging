#. WAF which takes two paramaters, camculates the sum and product of them and returns.
import logging
def sq(a,b):
    return((a*b),(a+b))

a=int(input())
b=int(input())
logging.basicConfig(filename= '6test.log',level=logging.DEBUG, format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
logging.debug(sq(a,b))

"""Output
3
5
20-May-21 15:27:46 - (15, 8)"""